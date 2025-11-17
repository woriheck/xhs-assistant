"""MCP Server for 小紅書 Content Generator."""

import json
from mcp.server.fastmcp import FastMCP
from .tools import extract_content, fetch_webpage, generate_xhs_post, refinement_xhs_post

# Initialize FastMCP server
mcp = FastMCP("xhs-assistant")


@mcp.tool()
async def generate_xhs_post_tool(
    content: str,
    iterations: int = 2
) -> str:
    """
    Generate a 小紅書 post using AI multi-agent workflow (generator → critic → improve).

    Args:
        content: The source content to generate a post from
        iterations: Number of critic-improve cycles (default: 2)

    Returns:
        JSON string with thread_id and final_post
    """
    input_data = {
        "content": content,
        "iterations": iterations
    }
    result = await generate_xhs_post(input_data)

    # Return thread_id and final post as JSON
    return json.dumps({
        "thread_id": result['thread_id'],
        "final_post": result['final_post']
    }, ensure_ascii=False)


@mcp.tool()
async def refinement_xhs_post_tool(
    thread_id: str,
    feedback: str,
    iterations: int = 1
) -> str:
    """
    Refine a post with user feedback.

    Args:
        thread_id: Thread ID from previous generate_xhs_post_tool call
        feedback: User feedback for refinement (e.g., "make it more casual", "add examples")
        iterations: Number of refinement cycles (default: 1)

    Returns:
        JSON string with thread_id and refined final_post
    """
    input_data = {
        "thread_id": thread_id,
        "feedback": feedback,
        "iterations": iterations
    }
    result = await refinement_xhs_post(input_data)

    # Return thread_id and refined post as JSON
    return json.dumps({
        "thread_id": result['thread_id'],
        "final_post": result['final_post']
    }, ensure_ascii=False)
