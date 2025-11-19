"""Main content generation tool with multi-agent workflow."""

import logging
import uuid
from langchain_core.messages import SystemMessage, HumanMessage
from ..agents import get_workflow
from ..agents.state import XHSPost
from ..agents.prompts import GENERATOR_PROMPT
from ..utils import log_conversation_flow

# Configure logger
logger = logging.getLogger(__name__)


async def generate_xhs_post(input_data: dict) -> dict:
    """
    Generate a 小紅書 post using LangGraph multi-agent workflow.

    This tool orchestrates the generator → critic → improve cycle using LangGraph.

    Args:
        input_data: dict containing:
            - content: The source content (text/extracted from file/web)
            - iterations: Number of critic-improve cycles (default: 2)

    Returns:
        dict with:
            - thread_id: Conversation thread ID for continuation
            - final_post: The generated post
    """
    # Extract parameters
    content = input_data.get("content", "")
    iterations = input_data.get("iterations", 2)

    # Generate unique thread ID for this conversation
    thread_id = str(uuid.uuid4())

    # Get the LangGraph workflow with checkpointer
    logger.info(f"🚀 Starting new conversation {thread_id}")
    workflow = get_workflow()

    # Initialize message chain with only SystemMessage
    # The first HumanMessage will be created by analyze_node
    messages = [
        SystemMessage(content=GENERATOR_PROMPT),
    ]

    # Initialize state for the workflow
    initial_state = {
        "content": content,  # Pass content directly in state
        "max_iterations": iterations,
        "iteration": 0,
        "post": XHSPost(title="", body=""),
        "messages": messages,
    }

    # Run workflow with thread ID for checkpointing
    config = {"configurable": {"thread_id": thread_id}}
    final_state = await workflow.ainvoke(initial_state, config)

    # Log conversation flow (only in debug mode)
    log_conversation_flow(final_state.get("messages", []))

    # Combine title and body for final post
    final_post = f"{final_state['post'].title}\n\n{final_state['post'].body}"

    # Return thread_id and final post
    return {
        "thread_id": thread_id,
        "final_post": final_post
    }


async def refinement_xhs_post(input_data: dict) -> dict:
    """
    Refine a post with user feedback.

    Args:
        input_data: dict containing:
            - thread_id: Thread ID from previous generation
            - feedback: User feedback for refinement
            - iterations: Number of additional refinement cycles (default: 1)

    Returns:
        dict with:
            - thread_id: Same thread ID
            - final_post: The refined post
    """
    thread_id = input_data.get("thread_id")
    feedback = input_data.get("feedback", "")
    iterations = input_data.get("iterations", 1)

    if not thread_id:
        raise ValueError("thread_id is required for continuation")

    logger.info(f"🔄 Continuing conversation {thread_id}")

    # Get workflow
    workflow = get_workflow()

    # Add user feedback as new message
    feedback_msg = HumanMessage(
        content=f"User feedback: {feedback}\n\nPlease refine the post based on this feedback."
    )

    # Resume from checkpoint with new input
    config = {"configurable": {"thread_id": thread_id}}

    # Update state with new message and iterations
    update_state = {
        "messages": [feedback_msg],
        "iteration": 0,  # Reset for new refinement cycles
        "max_iterations": iterations,
    }

    # Continue workflow from checkpoint
    final_state = await workflow.ainvoke(update_state, config)

    # Log conversation flow (only in debug mode)
    log_conversation_flow(final_state.get("messages", []), "Refinement Flow")

    # Combine title and body for final post
    final_post = f"{final_state['post'].title}\n\n{final_state['post'].body}"

    return {
        "thread_id": thread_id,
        "final_post": final_post
    }
