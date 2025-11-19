"""Entry point for 小紅書 Content Generator MCP Server."""

import os
import asyncio
import logging
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables once at startup
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

# Setup logging based on environment variable
from src.utils import setup_logging

# Control verbosity with environment variable
verbose = os.getenv("LOG_VERBOSE", "false").lower() == "true"
log_level = os.getenv("LOG_LEVEL", "INFO").upper()

setup_logging(level=log_level, verbose=verbose)
logger = logging.getLogger(__name__)

# Import and expose the FastMCP server object
from src.server import mcp

# Log startup message
logger.info("🚀 Starting 小紅書 Content Generator MCP Server...")
logger.info("📋 Available tools:")
logger.info("  • generate_xhs_post_tool - Generate 小紅書 posts")
logger.info("  • refinement_xhs_post_tool - Refine posts with feedback")
logger.info("✅ Server is ready and listening...")
logger.info("")

# Run the FastMCP server
if __name__ == "__main__":
    asyncio.run(mcp.run())
