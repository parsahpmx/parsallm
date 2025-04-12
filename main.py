import asyncio
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.bot import ChatBot
from src.config import Config
from src.utils import setup_logging, validate_message, format_response

# Initialize FastAPI app
app = FastAPI(title="ParsaLLM Chatbot")

# Initialize configuration
config = Config()

# Setup logging
setup_logging(config)

# Initialize chatbot
chatbot = ChatBot(config)

class Message(BaseModel):
    content: str
    sender: str

@app.post("/chat")
async def chat_endpoint(message: Message):
    """Handle incoming chat messages."""
    try:
        # Process message
        response = await chatbot.process_message(message.content)
        
        # Format and return response
        return format_response(response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=config.DEBUG)