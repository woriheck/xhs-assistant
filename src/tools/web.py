"""Web content fetching and extraction."""


async def fetch_webpage(url: str) -> dict:
    """
    Fetch and extract content from a webpage.

    Args:
        url: The URL to fetch content from

    Returns:
        dict with 'content' (extracted text), 'title', and 'url'
    """
    # TODO: Implement web fetching with httpx
    # TODO: Implement content extraction with BeautifulSoup

    return {
        "content": "",
        "title": "",
        "url": url
    }
