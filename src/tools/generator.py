"""Main content generation tool with multi-agent workflow."""

import sys
from langchain_core.messages import SystemMessage, HumanMessage
from ..agents import get_workflow
from ..agents.state import XHSPost
from ..agents.prompts import GENERATOR_PROMPT


async def generate_xhs_post(input_data: dict) -> dict:
    """
    Generate a 小紅書 post using LangGraph multi-agent workflow.

    This tool orchestrates the generator → critic → improve cycle using LangGraph.

    Args:
        input_data: dict containing:
            - content: The source content (text/extracted from file/web)
            - context: Optional additional context
            - iterations: Number of critic-improve cycles (default: 2)

    Returns:
        dict with:
            - final_post: The generated post only
    """
    # Extract parameters
    content = input_data.get("content", "")
    context = input_data.get("context", "")
    iterations = input_data.get("iterations", 2)

    # Combine content and context
    full_content = content
    if context:
        full_content = f"{content}\n\nAdditional context: {context}"

    # Get the LangGraph workflow
    print(f"🚀 Starting workflow with {iterations} iterations", file=sys.stderr, flush=True)
    workflow = get_workflow()

    # Initialize message chain
    # SystemMessage: Base instructions for authentic content creation
    # HumanMessage: Content to transform
    # (Custom structure will be added by preanalyse_node as HumanMessage)
    messages = [
        SystemMessage(content=GENERATOR_PROMPT),
        HumanMessage(content=f"Please generate a 小紅書 post from the following content:\n\n{full_content}"),
    ]

    # Initialize state for the workflow
    initial_state = {
        "max_iterations": iterations,
        "iteration": 0,
        "post": XHSPost(title="", body=""),
        "messages": messages,
    }

    # Run the workflow
    final_state = await workflow.ainvoke(initial_state)

    # Show conversation messages
    print("\n--- Conversation Flow ---", file=sys.stderr, flush=True)
    messages = final_state.get("messages", [])
    for i, msg in enumerate(messages, 1):
        msg_type = type(msg).__name__
        print(f"\n{i}. {msg_type}:", file=sys.stderr, flush=True)
        print(msg.content, file=sys.stderr, flush=True)
    print("\n--- End ---\n", file=sys.stderr, flush=True)

    # Combine title and body for final post
    final_post = f"{final_state['post'].title}\n\n{final_state['post'].body}"

    print(f"✅ Complete - Generated post ({len(final_post)} chars)", file=sys.stderr, flush=True)

    # Return only the final post
    return {
        "final_post": final_post
    }
