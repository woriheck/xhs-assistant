"""Logging configuration for XHS Assistant."""

import logging
import sys


def setup_logging(level: str = "INFO", verbose: bool = False):
    """
    Configure logging for the application.

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        verbose: If True, sets level to DEBUG and shows detailed conversation flow

    Usage:
        from src.utils.logging_config import setup_logging

        # Basic logging
        setup_logging()

        # Verbose logging (shows conversation flow)
        setup_logging(verbose=True)

        # Custom level
        setup_logging(level="WARNING")
    """
    # Set level based on verbose flag
    if verbose:
        level = "DEBUG"

    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stderr)
        ]
    )

    # Optionally suppress noisy libraries
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("anthropic").setLevel(logging.WARNING)


def log_conversation_flow(messages: list, title: str = "Conversation Flow", logger_name: str = None):
    """
    Log conversation messages in a structured way.

    Args:
        messages: List of conversation messages
        title: Title for the log section
        logger_name: Logger name to use (defaults to caller's logger)

    Usage:
        from src.utils.logging_config import log_conversation_flow

        log_conversation_flow(messages)
        log_conversation_flow(messages, title="Refinement Flow")
    """
    # Get logger
    logger = logging.getLogger(logger_name) if logger_name else logging.getLogger(__name__)

    # Only log if DEBUG level is enabled
    if not logger.isEnabledFor(logging.DEBUG):
        return

    logger.debug(f"\n{'='*50}")
    logger.debug(f"{title}")
    logger.debug(f"{'='*50}")

    for i, msg in enumerate(messages, 1):
        msg_type = type(msg).__name__
        logger.debug(f"\n{i}. {msg_type}:")
        logger.debug(f"{msg.content}")

    logger.debug(f"\n{'='*50}\n")
