"""MCP Server for 小紅書 Content Generator."""

from mcp.server.fastmcp import FastMCP
from .tools import extract_content, fetch_webpage, generate_xhs_post

# Initialize FastMCP server
mcp = FastMCP("xhs-assistant")


@mcp.tool()
async def extract_content_tool(file_path: str) -> str:
    """
    Extract content from PDF or image files.

    Args:
        file_path: Path to the file to extract content from

    Returns:
        Extracted content with metadata
    """
    result = await extract_content(file_path)
    return f"Extracted content:\n\n{result['content']}\n\nMetadata: {result['metadata']}"


@mcp.tool()
async def fetch_webpage_tool(url: str) -> str:
    """
    Fetch and extract content from a webpage URL.

    Args:
        url: The URL to fetch content from

    Returns:
        Page title and extracted content
    """
    result = await fetch_webpage(url)
    return f"Title: {result['title']}\n\nContent:\n{result['content']}"


@mcp.tool()
async def generate_xhs_post_tool(
    content: str,
    context: str = "",
    iterations: int = 2
) -> str:
    """
    Generate a 小紅書 post using AI multi-agent workflow (generator → critic → improve).

    Args:
        content: The source content to generate a post from
        context: Optional additional context or instructions
        iterations: Number of critic-improve cycles (default: 2)

    Returns:
        The final generated post (process log is dumped to stderr)
    """
    input_data = {
        "content": content,
        "context": context,
        "iterations": iterations
    }
    result = await generate_xhs_post(input_data)

    # Return only the final post
    return result['final_post']
