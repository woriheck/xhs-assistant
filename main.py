"""Entry point for 小紅書 Content Generator MCP Server."""

import sys
import asyncio
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables once at startup
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

# Import and expose the FastMCP server object
from src.server import mcp

# Log startup message to stderr
print("🚀 Starting 小紅書 Content Generator MCP Server...", file=sys.stderr)
print("📋 Available tools:", file=sys.stderr)
print("  • extract_content_tool - Extract from PDF/images", file=sys.stderr)
print("  • fetch_webpage_tool - Get content from URLs", file=sys.stderr)
print("  • generate_xhs_post_tool - Generate 小紅書 posts", file=sys.stderr)
print("✅ Server is ready and listening...", file=sys.stderr)
print("", file=sys.stderr)

# Run the FastMCP server
if __name__ == "__main__":
    asyncio.run(mcp.run())
