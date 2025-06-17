A Python command-line AI agent built while following the Boot.dev course "Build an AI Agent in Python". This LLM-powered tool uses Google's Gemini API to interact with and modify Python code, demonstrating fundamental concepts of AI agents and function calling.

## Features
- Google Gemini API integration for NLP
- Command-line interface with verbose mode
- File system inspection capabilities
- Function calling architecture for extensibility
- Secure API key management with environment variables

## Installation
Clone the repository:
```bash
git clone https://github.com/Armivio/boot-ai-agent
cd boot-ai-agent
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Set up your Google Gemini API key:
```bash
# Create a .env file in the project root
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Usage
Basic usage:
```bash
python main.py "Your prompt here"
```

Verbose mode (shows token usage):
```bash
python main.py "Your prompt here" --verbose
```

## Project Structure
```
boot-ai-agent/
├── main.py                 # Main CLI application
├── functions/              # Agent tool functions
│   └── get_files_info.py  # File system inspection tool
├── calculator/             # Example project for testing
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── requirements.txt        # Python dependencies
└── README.md
```

## Testing
Test the calculator example:
```bash
cd calculator
python main.py "3 + 5 * 2"
python tests.py
```

## Credits
This project was developed as part of the boot.dev course "Build an AI Agent in Python". The "calculator" folder and its files were provided by the course. The course structure and learning objectives were provided by boot.dev, but all implementation code was written during the learning process.