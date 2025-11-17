"""LangGraph workflow for 小紅書 content generation."""

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from .state import WorkflowState
from .nodes import analyze_node, generator_node, critic_node, formatting_node, should_continue


# Create in-memory checkpointer (simple and synchronous)
checkpointer = MemorySaver()


def get_workflow():
    """
    Create the 小紅書 content generation workflow with checkpointing.

    Flow:
      analyze → generator → should_continue?
                       ├─ yes → critic → generator (content improvement)
                       └─ no  → formatting → END (auto-fix format)

    The formatting node validates and auto-fixes platform requirements
    (character limits, structure) without changing content.

    Returns:
        Compiled LangGraph workflow with checkpointer
    """
    # Create graph with state schema
    workflow = StateGraph(WorkflowState)

    # Add nodes
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("generator", generator_node)
    workflow.add_node("critic", critic_node)
    workflow.add_node("formatting", formatting_node)

    # Set entry point to analyze
    workflow.set_entry_point("analyze")

    # Add edge from analyze to generator
    workflow.add_edge("analyze", "generator")

    # Add conditional edges from generator
    workflow.add_conditional_edges(
        "generator",
        should_continue,
        {
            "critic": "critic",      # Continue to critic for content improvement
            "end": "formatting",     # Go to formatting for final cleanup
        }
    )

    # Add edge from critic back to generator (for improvement)
    workflow.add_edge("critic", "generator")

    # Add edge from formatting to END
    workflow.add_edge("formatting", END)

    # Compile with checkpointer
    # Will save state with thread_id for continuation
    return workflow.compile(checkpointer=checkpointer)
