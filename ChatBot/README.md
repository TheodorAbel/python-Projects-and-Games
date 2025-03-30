# AI Chatbot with Authentication

## Description
This project is an AI-powered chatbot with user authentication. Users can register, log in, and interact with the chatbot, which uses OpenAI's API to generate responses. Chat history is stored in an SQLite database for future reference.

## Features
- User registration and authentication
- AI-generated responses using OpenAI API
- Chat history storage in SQLite database
- Interactive command-line interface

## Technologies Used
- **Python**
- **OpenAI API**
- **SQLite3**

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- `pip` (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/your-repo/chatbot-project.git
cd chatbot-project
```

### Install Dependencies
```bash
pip install openai sqlite3
```

### Set Up Configuration
Create a `config.py` file and add your OpenAI API key:
```python
OPENAI_API_KEY = "your-openai-api-key"
DATABASE_NAME = "chatbot.db"
```

## Usage
Run the chatbot with:
```bash
python main.py
```

### User Options
1. **Register**: Create a new account
2. **Login**: Access your account and chat with the AI
3. **Exit**: Close the program

Once logged in, type your messages to chat with the AI. Type `exit` or `quit` to end the conversation.

## Database Structure
The SQLite database stores user credentials and chat history:
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    message TEXT,
    response TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Troubleshooting
### "ModuleNotFoundError: No module named 'openai'"
Run:
```bash
pip install openai
```

### "Error: module 'openai' has no attribute 'chat_completions'"
Ensure you are using `openai.ChatCompletion.create()` for GPT models.

### "Error: Client.__init__() got an unexpected keyword argument 'proxies'"
Ensure you are using OpenAI's latest API version:
```bash
pip install --upgrade openai
```

## License
This project is open-source and free to use.

