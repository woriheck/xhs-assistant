"""Logging utilities for workflow execution."""

import sys
import json
from typing import List, Dict, Any


def log_process_to_stderr(process_log: List[Dict[str, Any]], iterations: int) -> None:
    """
    Log workflow process to stderr in a formatted way.

    Args:
        process_log: List of process log entries from workflow execution
        iterations: Number of iterations completed
    """
    print("=" * 60, file=sys.stderr)
    print("PROCESS LOG", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    for entry in process_log:
        print(json.dumps(entry, ensure_ascii=False, indent=2), file=sys.stderr)
        print("-" * 60, file=sys.stderr)

    print(f"Completed {iterations} iteration(s)", file=sys.stderr)
    print("=" * 60, file=sys.stderr)


def log_workflow_start(content_preview: str, iterations: int) -> None:
    """
    Log workflow start to stderr.

    Args:
        content_preview: Preview of content being processed (first 100 chars)
        iterations: Number of iterations to run
    """
    print("=" * 60, file=sys.stderr)
    print("🚀 WORKFLOW START", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"Content: {content_preview[:100]}...", file=sys.stderr)
    print(f"Max iterations: {iterations}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)


def log_workflow_end(final_post_preview: str) -> None:
    """
    Log workflow completion to stderr.

    Args:
        final_post_preview: Preview of final post (first 100 chars)
    """
    print("=" * 60, file=sys.stderr)
    print("✅ WORKFLOW COMPLETE", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    print(f"Final post: {final_post_preview[:100]}...", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
