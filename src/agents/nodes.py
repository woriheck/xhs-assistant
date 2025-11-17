"""Reusable node functions for LangGraph workflows."""

import sys
from typing import Literal
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from ..utils.llm import base_llm
from .validators.xhs_post_validators import validate_post, format_validation_feedback
from .state import XHSPost
from .prompts import CRITIC_PROMPT, ANALYZE_PROMPT, ANALYZE_INSTRUCTION_TEMPLATE, FORMATTING_PROMPT


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



async def analyze_node(state: dict) -> dict:
    """
    Analyze node: Analyzes content and generates custom structure dynamically.

    Args:
        state: Current workflow state

    Returns:
        Dict with state updates (messages with instruction + content + analysis)
    """
    # Get content directly from state
    content = state.get("content", "")

    # Build analyze prompt
    prompt = ANALYZE_PROMPT.format(content=content)

    # Use structured output with Pydantic model
    structured_llm = base_llm.with_structured_output(ContentAnalysis)

    # Get content analysis from LLM
    analysis: ContentAnalysis = await structured_llm.ainvoke(prompt)

    # Create the HumanMessage with instruction + content + analysis
    # This combines what was previously two separate messages
    message = HumanMessage(
        content=ANALYZE_INSTRUCTION_TEMPLATE.format(
            content=content,
            target_audience=analysis.target_audience,
            audience_needs=analysis.audience_needs,
            tone_guidance=analysis.tone_guidance,
            recommended_structure=analysis.recommended_structure
        )
    )

    return {
        "messages": [message],
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
    Critic node: Critiques content quality (tone, authenticity, audience fit).

    Args:
        state: Current workflow state

    Returns:
        Dict with state updates (messages)
    """
    # Build critic prompt
    critic_prompt = CRITIC_PROMPT.format(title=state['post'].title, body=state['post'].body)

    # Get critique from LLM
    response = await base_llm.ainvoke(critic_prompt)

    # Add critique as feedback message
    critique_message = HumanMessage(
        content=f"Critique:\n{response.content}\n\nPlease improve the post based on this feedback."
    )

    return {
        "messages": [critique_message],
    }


async def formatting_node(state: dict) -> dict:
    """
    Formatting node: Uses LLM to improve formatting and ensure length compliance.

    Args:
        state: Current workflow state

    Returns:
        Dict with formatted post
    """
    from ..agents.validators.xhs_post_validators import TITLE_MAX_CHARS, BODY_MAX_CHARS

    post = state['post']

    # Get current lengths
    title_length = len(post.title)
    body_length = len(post.body)

    # Build formatting prompt
    prompt = FORMATTING_PROMPT.format(
        title=post.title,
        body=post.body,
        title_max=TITLE_MAX_CHARS,
        body_max=BODY_MAX_CHARS,
        title_length=title_length,
        body_length=body_length
    )

    # Use structured output to get formatted post
    structured_llm = base_llm.with_structured_output(XHSPost)
    formatted_post: XHSPost = await structured_llm.ainvoke(prompt)

    # Log formatting results
    new_title_length = len(formatted_post.title)
    new_body_length = len(formatted_post.body)

    if title_length != new_title_length:
        print(f"📝 Title adjusted: {title_length} → {new_title_length} chars", file=sys.stderr, flush=True)

    if body_length != new_body_length:
        print(f"📝 Body adjusted: {body_length} → {new_body_length} chars", file=sys.stderr, flush=True)

    if title_length == new_title_length and body_length == new_body_length:
        print(f"✅ Formatting optimized (no length changes needed)", file=sys.stderr, flush=True)

    return {
        "post": formatted_post,
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
