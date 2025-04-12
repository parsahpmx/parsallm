# ParsaLLM Chatbot

A powerful LangChain-powered chatbot built with Python, featuring real-time communication through MCP (Multi-Channel Platform) integration.

## Features

- 🤖 Intelligent responses using LangChain and LLMs
- 🔄 Real-time communication via MCP
- 🎯 Modular and extensible architecture
- 📝 Message analysis and processing
- 🔧 Easy configuration and deployment

## Project Structure

```
parsallm/
├── src/
│   ├── __init__.py
│   ├── bot.py
│   ├── config.py
│   └── utils.py
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parsahpmx/parsallm.git
   cd parsallm
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Configuration

Configure the following environment variables in your `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
MCP_API_KEY=your_mcp_api_key
MODEL_NAME=gpt-3.5-turbo
DEBUG=False
```

## Usage

Run the chatbot:

```bash
python main.py
```

## Development

### Adding New Features

1. Create new modules in the `src` directory
2. Update the configuration in `config.py`
3. Implement new functionality in modular components
4. Update main.py to integrate new features

### Testing

The project includes a basic test suite. Run tests with:

```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository.