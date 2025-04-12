import os
from dotenv import load_dotenv
from pydantic import BaseSettings

class Config(BaseSettings):
    """Configuration management for the chatbot."""
    
    # Load environment variables
    load_dotenv()
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    MCP_API_KEY: str = os.getenv('MCP_API_KEY', '')
    
    # Model Configuration
    MODEL_NAME: str = os.getenv('MODEL_NAME', 'gpt-3.5-turbo')
    MAX_TOKENS: int = int(os.getenv('MAX_TOKENS', 2000))
    TEMPERATURE: float = float(os.getenv('TEMPERATURE', 0.7))
    
    # Application Configuration
    DEBUG: bool = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    
    class Config:
        env_file = '.env'
        case_sensitive = True