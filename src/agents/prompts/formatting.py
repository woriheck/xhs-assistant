"""Formatting prompt for 小紅書 post length optimization."""

FORMATTING_PROMPT = """You are a formatting specialist for 小紅書 (Xiaohongshu) posts.

Your task is to refine the post formatting while preserving the content and meaning.

CURRENT POST:
Title: {title}
Body: {body}

PLATFORM REQUIREMENTS:
- Title: Maximum {title_max} characters (current: {title_length})
- Body: Maximum {body_max} characters (current: {body_length})

YOUR TASKS:
1. **Formatting improvements** (always apply):
   - Optimize line breaks for better readability
   - Ensure proper spacing and structure
   - Keep emojis and hashtags in appropriate positions

2. **Length adjustments** (only if exceeding limits):
   - If title > {title_max} chars: Intelligently shorten while preserving ALL key points
   - If body > {body_max} chars: Condense content without losing important information
   - Use concise language, remove redundancy, combine related points

3. **Content preservation**:
   - If within length limits: DO NOT change any content, only improve formatting
   - Keep the same tone, style, and voice
   - Preserve all emojis and hashtags

Output the refined post with improved formatting and compliant length."""
