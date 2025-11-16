"""LangGraph workflow for 小紅書 content generation."""

from langgraph.graph import StateGraph, END
from .state import WorkflowState
from .nodes import preanalyse_node, generator_node, critic_node, should_continue


def get_workflow():
    """
    Create the 小紅書 content generation workflow.

    Flow:
      preanalyse → generator → (should_continue?)
                          ├─ yes → critic → generator
                          └─ no  → END

    Returns:
        Compiled LangGraph workflow
    """
    # Create graph with state schema
    workflow = StateGraph(WorkflowState)

    # Add nodes
    workflow.add_node("preanalyse", preanalyse_node)
    workflow.add_node("generator", generator_node)
    workflow.add_node("critic", critic_node)

    # Set entry point to preanalyse
    workflow.set_entry_point("preanalyse")

    # Add edge from preanalyse to generator
    workflow.add_edge("preanalyse", "generator")

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
