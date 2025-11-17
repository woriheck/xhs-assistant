"""Prompts for 小紅書 content generation workflow."""

from .generator import GENERATOR_PROMPT
from .critic import CRITIC_PROMPT
from .analyze import ANALYZE_PROMPT, ANALYZE_INSTRUCTION_TEMPLATE
from .formatting import FORMATTING_PROMPT

__all__ = [
    "GENERATOR_PROMPT",
    "CRITIC_PROMPT",
    "ANALYZE_PROMPT",
    "ANALYZE_INSTRUCTION_TEMPLATE",
    "FORMATTING_PROMPT",
]
