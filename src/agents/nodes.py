"""Reusable node functions for LangGraph workflows."""

import sys
from typing import Literal
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from ..utils.llm import base_llm
from .validators.xhs_post_validators import validate_post, format_validation_feedback
from .state import XHSPost
from .prompts import CRITIC_PROMPT, PREANALYSE_PROMPT


class ContentAnalysis(BaseModel):
    """Structured output for content analysis and custom structure generation."""
    target_audience: str = Field(
        description="Specific audience who would be most interested in this content (e.g., 'Tech leaders managing AI teams', 'Senior engineers evaluating tools', 'Product managers launching features')"
    )
    audience_needs: str = Field(
        description="What this audience cares about and their key concerns/interests"
    )
    recommended_structure: str = Field(
        description="Custom post structure tailored to this specific content and audience (step-by-step outline)"
    )
    tone_guidance: str = Field(
        description="How to write for this audience (voice, style, what to emphasize, what to avoid)"
    )



async def preanalyse_node(state: dict) -> dict:
    """
    Preanalyse node: Analyzes content and generates custom structure dynamically.

    Args:
        state: Current workflow state

    Returns:
        Dict with state updates (messages with custom structure and tone)
    """
    # Extract content from the first user message
    messages = state.get("messages", [])
    content = ""
    for msg in messages:
        if isinstance(msg, HumanMessage):
            content = msg.content
            break

    # Build preanalyse prompt
    prompt = PREANALYSE_PROMPT.format(content=content)

    # Use structured output with Pydantic model
    structured_llm = base_llm.with_structured_output(ContentAnalysis)

    # Get content analysis from LLM
    # Note: Logs from inside LangGraph nodes don't show up due to buffering
    # All logging is done in generator.py after workflow completes
    analysis: ContentAnalysis = await structured_llm.ainvoke(prompt)

    # Add custom structure as HumanMessage (recitation)
    # Include audience context, tone guidance, and custom structure
    structure_msg = HumanMessage(
        content=f"""TARGET AUDIENCE: {analysis.target_audience}

WHAT THEY CARE ABOUT:
{analysis.audience_needs}

TONE & VOICE GUIDANCE:
{analysis.tone_guidance}

RECOMMENDED STRUCTURE FOR THIS POST:
{analysis.recommended_structure}"""
    )

    return {
        "messages": [structure_msg],  # Append custom structure
    }


async def generator_node(state: dict) -> dict:
    """
    Generator node: Creates or improves a 小紅書 post using message chain.

    Args:
        state: Current workflow state

    Returns:
        Dict with state updates (title, body, iteration, messages, process_log)
    """
    # Get current iteration
    iteration = state.get("iteration", 0)

    # Get message history (conversation so far)
    messages = state.get("messages", [])

    # Use structured output with Pydantic model
    structured_llm = base_llm.with_structured_output(XHSPost)

    # Call LLM with message chain
    post: XHSPost = await structured_llm.ainvoke(messages)

    # Create AI response message with the generated post
    ai_message = AIMessage(
        content=f"Title: {post.title}\n\nBody:\n{post.body}"
    )

    # Return state updates
    return {
        "iteration": iteration + 1,
        "messages": [ai_message],
        "post": post,
    }

async def critic_node(state: dict) -> dict:
    """
    Critic node: Validates and critiques the current post.

    Args:
        state: Current workflow state

    Returns:
        Dict with state updates (messages)
    """
    # Create and validate post
    validation_results = validate_post(state['post'])

    # Build critic prompt
    critic_prompt = CRITIC_PROMPT.format(title=state['post'].title, body=state['post'].body)

    # Get critique from LLM
    response = await base_llm.ainvoke(critic_prompt)

    # Get validation feedback
    validation_feedback = format_validation_feedback(validation_results)

    # Combine critique and validation
    critique_message = HumanMessage(
        content=f"Critique:\n{response.content}{validation_feedback}\n\nPlease improve the post based on this feedback."
    )

    return {
        "messages": [critique_message],
    }

def should_continue(state: dict) -> Literal["critic", "end"]:
    """
    Routing function: Decides whether to continue to critic or end.

    Args:
        state: Current workflow state

    Returns:
        "critic" if should continue iterating, "end" if done
    """
    # Check if we should continue to critic or end the workflow
    # Note: iteration was already incremented by generator_node
    current_iteration = state.get("iteration", 0)
    max_iterations = state.get("max_iterations", 2)

    if current_iteration <= max_iterations:
        return "critic"
    return "end"
