import logging
from datetime import datetime
from typing import Any, Dict
from .config import Config

def setup_logging(config: Config) -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=config.LOG_LEVEL,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def validate_message(message: Dict[str, Any]) -> bool:
    """Validate incoming message format."""
    required_fields = ['content', 'sender']
    return all(field in message for field in required_fields)

def format_response(response: str) -> Dict[str, Any]:
    """Format bot response for MCP."""
    return {
        'content': response,
        'type': 'text',
        'timestamp': datetime.now().isoformat()
    }