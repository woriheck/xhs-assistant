"""LangGraph state schemas for workflows."""

from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field

class XHSPost(BaseModel):
    """Structured output for 小紅書 post."""
    title: str = Field(description="Post title (max 64 characters)")
    body: str = Field(description="Post body content (max 10,000 characters)")

class WorkflowState(TypedDict):
    """State for the preanalyse → generator → critic workflow.

    Uses TypedDict with Annotated reducers for proper state management.
    """

    # Message-based conversation history
    messages: Annotated[list, add_messages]

    # Working state - structured post
    post: XHSPost
    iteration: int
    max_iterations: int
