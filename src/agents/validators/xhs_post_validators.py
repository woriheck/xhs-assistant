"""小紅書 post validation utilities."""

from ..state import XHSPost

# Platform limits
TITLE_MAX_CHARS = 64
BODY_MAX_CHARS = 10000

# Optimal ranges for engagement
TITLE_OPTIMAL_MIN = 10
TITLE_OPTIMAL_MAX = 20
BODY_OPTIMAL_MIN = 500
BODY_OPTIMAL_MAX = 2000
BODY_MAX_CHARS_PER_LINE = 20

def validate_post(post: XHSPost) -> dict:
    """
    Validate if a post meets 小紅書 guidelines.

    Args:
        post: XHSPost object with title and body

    Returns:
        dict with:
            - valid: bool
            - issues: list of validation issues
            - suggestions: list of improvements
            - stats: character counts and other metrics
    """
    issues = []
    suggestions = []

    # Get title and body from post object
    title = post.title
    body = post.body

    title_len = len(title)
    body_len = len(body)
    total_len = title_len + body_len

    # Check title length
    if title_len > TITLE_MAX_CHARS:
        issues.append(f"Title too long: {title_len}/{TITLE_MAX_CHARS} characters")
        suggestions.append(f"Shorten title by {title_len - TITLE_MAX_CHARS} characters")
    elif title_len < TITLE_OPTIMAL_MIN:
        suggestions.append(f"Title is short ({title_len} chars). Consider {TITLE_OPTIMAL_MIN}-{TITLE_OPTIMAL_MAX} chars for better engagement")
    elif title_len > TITLE_OPTIMAL_MAX:
        suggestions.append(f"Title is long ({title_len} chars). Consider {TITLE_OPTIMAL_MIN}-{TITLE_OPTIMAL_MAX} chars for better engagement")

    # Check body length
    if body_len > BODY_MAX_CHARS:
        issues.append(f"Body too long: {body_len}/{BODY_MAX_CHARS} characters")
        suggestions.append(f"Reduce body by {body_len - BODY_MAX_CHARS} characters")
    elif body_len < BODY_OPTIMAL_MIN:
        suggestions.append(f"Body is short ({body_len} chars). Consider {BODY_OPTIMAL_MIN}-{BODY_OPTIMAL_MAX} chars for better engagement")
    elif body_len > BODY_OPTIMAL_MAX:
        suggestions.append(f"Body is long ({body_len} chars). Consider {BODY_OPTIMAL_MIN}-{BODY_OPTIMAL_MAX} chars for mobile reading")

    # Check for hashtags
    full_post = f"{title}\n{body}"
    if '#' not in full_post:
        suggestions.append("Add hashtags for better discoverability")

    # Count emojis (rough check)
    emoji_count = sum(1 for char in full_post if ord(char) > 0x1F300)
    if emoji_count == 0:
        suggestions.append("Add emojis for better engagement")
    elif emoji_count > 20:
        suggestions.append(f"Too many emojis ({emoji_count}). Use them sparingly")

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "suggestions": suggestions,
        "stats": {
            "title_length": title_len,
            "body_length": body_len,
            "total_length": total_len,
            "emoji_count": emoji_count,
            "has_hashtags": '#' in post
        }
    }


def format_validation_feedback(validation_results: dict) -> str:
    """
    Format validation results into feedback string for critique message.

    Args:
        validation_results: Validation dict from validate_post()

    Returns:
        Formatted validation feedback string (empty if no issues/suggestions)
    """
    feedback = ""

    if validation_results['issues']:
        feedback += "\n\nValidation Issues:\n"
        feedback += "\n".join(f"- {issue}" for issue in validation_results['issues'])

    if validation_results['suggestions']:
        feedback += "\n\nSuggestions:\n"
        feedback += "\n".join(f"- {sug}" for sug in validation_results['suggestions'])

    return feedback
