"""Basic workflow: generator → critic → improve → end."""

from langgraph.graph import StateGraph, END
from ..state import WorkflowState
from ..nodes import generator_node, critic_node, should_continue


def create_basic_workflow():
    """
    Create the basic 小紅書 content generation workflow.

    Flow:
        START
          ↓
        generator (creates post)
          ↓
        should_continue?
          ├─→ YES → critic (critiques with validation tool)
          │           ↓
          │         generator (improves post)
          │           ↓ (loop)
          └─→ NO → END

    Returns:
        Compiled LangGraph workflow
    """
    # Create graph with state schema (modern pattern)
    workflow = StateGraph(WorkflowState)

    # Add nodes
    workflow.add_node("generator", generator_node)
    workflow.add_node("critic", critic_node)

    # Set entry point
    workflow.set_entry_point("generator")

    # Add conditional edges from generator
    workflow.add_conditional_edges(
        "generator",
        should_continue,
        {
            "critic": "critic",  # Continue to critic
            "end": END,          # Finish workflow
        }
    )

    # Add edge from critic back to generator (for improvement)
    workflow.add_edge("critic", "generator")

    # Compile and return
    return workflow.compile()
