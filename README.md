# 🤖 Chatbot CAG by Liv_IA DEMO

A context-aware chatbot application built with Streamlit and Google's Gemini AI. This application demonstrates **Context-Aware Generation (CAG)**, where the chatbot maintains conversation context across messages for more natural and coherent interactions.

## ✨ Features

- **Context-Aware Generation (CAG)**: Maintains full conversation history, allowing the model to understand context from previous messages
- **Modern Chat Interface**: Clean, intuitive chat UI built with Streamlit's chat components
- **Real-time Responses**: Interactive chat experience with instant feedback
- **Powered by Gemini 2.5 Flash**: Fast and efficient AI responses using Google's latest Gemini model
- **Session Management**: Conversation history persists during the session
- **Easy Setup**: Simple configuration with environment variables

## 🚀 Getting Started

### Prerequisites

- Python 3.12 
- Google Gemini API key 

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/liviasouza01/chat_CAG.git
   cd chat_CAG
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env_example .env
   ```
   
   Edit `.env` and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

### Running the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📖 How It Works

### Context-Aware Generation (CAG)

Unlike traditional chatbots that treat each message independently, CAG maintains the entire conversation history as context. When you send a new message:

1. **Context Building**: All previous user-assistant message pairs are compiled into a conversation context
2. **Prompt Construction**: The new message is combined with the historical context
3. **Model Processing**: Gemini 2.5 Flash processes the full context-aware prompt
4. **Response Generation**: The model generates a response that understands the conversation flow

### Example

```
User: "My name is Alice and I'm 25 years old"
Bot: "Nice to meet you, Alice! How can I help you today?"

User: "What's my name?"
Bot: "Your name is Alice."  ← CAG remembers from context!
```

## 🏗️ Project Structure

```
chat_CAG/
├── app.py              # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env_example        # Environment variables template
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── venv/               # Virtual environment (not tracked)
```

## 🛠️ Technologies Used

- **Streamlit** (1.51.0): Web framework for the chat interface
- **Google Generative AI** (0.8.5): Gemini 2.5 Flash model integration
- **Python-dotenv** (1.2.1): Environment variable management
- **Python 3.12**: Runtime environment

## ⚙️ Configuration

The application uses a single environment variable:

- `GOOGLE_API_KEY`: Your Google Gemini API key (required)

Create a `.env` file in the project root with your API key:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

## 💡 Usage Tips

- **Send messages**: Type in the chat input at the bottom and press Enter
- **Conversation context**: The bot remembers everything you've discussed in the session
- **New session**: Refresh the page to start a new conversation

## 🔒 Security Notes

- Never commit your `.env` file to version control
- The `.env` file is already included in `.gitignore`
- Keep your API keys secure and don't share them publicly

