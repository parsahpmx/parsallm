from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from .config import Config

class ChatBot:
    """Main chatbot class implementing the core conversation logic."""
    
    def __init__(self, config: Config):
        self.config = config
        self.chat_model = ChatOpenAI(
            model_name=config.MODEL_NAME,
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS
        )
        self.system_message = SystemMessage(content="You are a helpful AI assistant.")
    
    async def process_message(self, message: str) -> str:
        """Process incoming messages and generate responses."""
        messages = [
            self.system_message,
            HumanMessage(content=message)
        ]
        
        try:
            response = await self.chat_model.agenerate([messages])
            return response.generations[0][0].text
        except Exception as e:
            if self.config.DEBUG:
                return f"Error processing message: {str(e)}"
            return "I apologize, but I encountered an error processing your message."