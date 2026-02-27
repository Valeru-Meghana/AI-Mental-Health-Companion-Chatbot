import streamlit as st
import requests
import os
from dotenv import load_dotenv

# -----------------------------
# Load API key
# -----------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env")
    st.stop()

API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"

# -----------------------------
# Streamlit UI settings
# -----------------------------
st.set_page_config(page_title="Groq LLM Mental Health Chatbot", page_icon="🧠")

# Dark background
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    ::placeholder {
        color: #AAAAAA;
    }
    .scrollable-container {
        max-height: 70vh;
        overflow-y: auto;
        padding-right: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#00FF00;'>🧠 Groq LLM Mental Health Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#CCCCCC;'>Talk to the chatbot for emotional support or mental health guidance. I'm here to listen!</p>", unsafe_allow_html=True)

# -----------------------------
# Initialize conversation
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly and empathetic mental health support chatbot."}
    ]

# -----------------------------
# Display conversation in scrollable container
# -----------------------------
container = st.container()
with container:
    for msg in st.session_state.messages[1:]:  # skip system message
        if msg["role"] == "user":
            st.markdown(f"""
                <div style="display:flex; justify-content:flex-end; margin-bottom:8px;">
                    <div style="background-color:#25D366; color:#000000; padding:10px 15px; 
                                border-radius:15px 15px 0px 15px; max-width:80%;">
                        <strong>You:</strong> {msg['content']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="display:flex; justify-content:flex-start; margin-bottom:8px;">
                    <div style="background-color:#2C2C2C; color:#FFFFFF; padding:10px 15px; 
                                border-radius:15px 15px 15px 0px; box-shadow: 0px 1px 3px rgba(0,0,0,0.5); max-width:80%;">
                        <strong>Bot:</strong> {msg['content']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

# -----------------------------
# Input at the bottom with auto-clear
# -----------------------------
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        payload = {
            "model": MODEL_NAME,
            "messages": st.session_state.messages,
            "temperature": 0.7,
            "max_tokens": 512
        }

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        data = response.json()

        bot_reply = data["choices"][0]["message"]["content"] if "choices" in data and data["choices"] else "⚠️ Couldn't get a valid response from the model."

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        st.session_state.messages.append({"role": "assistant", "content": "⚠️ Error calling Groq LLM."})
        st.error(str(e))