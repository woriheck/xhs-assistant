"""LangGraph workflow definitions."""

from .basic import create_basic_workflow

# Workflow registry
WORKFLOWS = {
    "basic": create_basic_workflow,
    # Add more workflows here as needed
}


def get_workflow(workflow_type: str = "basic"):
    """
    Factory function to get the appropriate workflow graph.

    Args:
        workflow_type: Type of workflow to create ("basic", etc.)

    Returns:
        Compiled LangGraph workflow

    Raises:
        ValueError: If workflow_type is not recognized
    """
    factory = WORKFLOWS.get(workflow_type)
    if factory is None:
        raise ValueError(
            f"Unknown workflow type: {workflow_type}. "
            f"Available: {list(WORKFLOWS.keys())}"
        )
    return factory()


__all__ = ["get_workflow", "create_basic_workflow", "WORKFLOWS"]
