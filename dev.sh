#!/bin/bash
# Development script for testing MCP server with auto-reload

echo "🔧 Starting MCP Inspector for development..."
echo "📝 Changes to your code will be reflected on page reload"
echo "🌐 Open the URL shown below in your browser"
echo ""

cd "$(dirname "$0")"
uv run mcp dev main.py
