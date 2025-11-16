"""Shared LLM configuration and initialization."""

import os
from langchain.chat_models import init_chat_model

# Configuration (loaded once in main.py)
MODEL_PROVIDER = os.environ.get("MODEL_PROVIDER", "deepseek")
MODEL_NAME = os.environ.get("MODEL_NAME", "deepseek-chat")


def get_api_key():
    """Get the appropriate API key for the provider."""
    if MODEL_PROVIDER == "deepseek":
        return os.environ.get("DEEPSEEK_API_KEY")
    else:
        return os.environ.get("OPENAI_API_KEY")


# Initialize base LLM - shared by all agents
base_llm = init_chat_model(
    model=MODEL_NAME,
    model_provider=MODEL_PROVIDER,
    api_key=get_api_key(),
    max_tokens=2048
)
