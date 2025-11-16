"""Prompts for 小紅書 content generation workflow."""

from .generator import GENERATOR_PROMPT
from .critic import CRITIC_PROMPT
from .preanalyse import PREANALYSE_PROMPT

__all__ = [
    "GENERATOR_PROMPT",
    "CRITIC_PROMPT",
    "PREANALYSE_PROMPT",
]
