# AI-Mental-Health-Companion-Chatbot
A WhatsApp-style mental health chatbot using Groq LLM. Provides empathetic support, anxiety relief, and guidance with a dark-mode chat interface. User messages are auto-cleared and pinned at the bottom for smooth conversation.


## Features

* WhatsApp-style dark mode chat UI
* User messages on the right (green bubbles)
* Bot messages on the left (dark gray bubbles)
* Input box pinned at the bottom for smooth chatting
* Input automatically clears after sending a message
* Conversation history preserved in the session
* Works with Groq LLM (`llama-3.1-8b-instant`)

---

## Folder Structure

```
MentalHealthChatbot/
│
├── app.py                 # Main Streamlit app
├── .env                   # Store your Groq API key here
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/MentalHealthChatbot.git
cd MentalHealthChatbot
```

2. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your Groq API key in a `.env` file:

```bash
GROQ_API_KEY=your_actual_groq_api_key_here
```

5. Run the Streamlit app:

```bash
streamlit run app.py
```

6. Open the link in your browser and start chatting!

---

## Dependencies

* Streamlit
* Requests
* Python-dotenv

Install via:

```bash
pip install -r requirements.txt
```

---

## Notes

* The chatbot uses the Groq API (`llama-3.1-8b-instant`). Make sure your API key is active.
* Everything typed in the chatbot is confidential within the session.

---

## License

MIT License
