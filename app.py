import os

# Fix: Redirect Streamlit config path to a local writable folder

config_dir = os.path.join(os.getcwd(), ".streamlit")
os.makedirs(config_dir, exist_ok=True)


# Optional: Disable Streamlit writing config files
os.environ["STREAMLIT_DISABLE_CONFIG_MUTATIONS"] = "true"
import streamlit as st
import requests
from dotenv import load_dotenv  # ✅ Load environment variables from .env

load_dotenv()  # ✅ Call this before using os.getenv()

# ---- Page setup ----
st.set_page_config(page_title="Memo AI - Book Writing Assistant", layout="centered")
st.title("📚 Memo AI - Book Writing Assistant")
st.markdown("Start writing chapters, outlines, and full books with the help of AI.")

# ---- User inputs ----
book_title = st.text_input("📘 Book Title")
Genre = st.selectbox("🎨 Genre", ["Inspiring", "Casual", "Dramatic", "Professional"])
user_query = st.text_area("✍️ Describe your idea or prompt:")

# ---- Chat history setup ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- Load API key from environment ----
API_KEY = os.getenv("MEMO_API_KEY")
API_ENDPOINT = "https://api.dify.ai/v1/chat-messages"

# ---- Generate with Memo AI ----
if st.button("Generate with Memo AI") and user_query.strip() != "":
    if not API_KEY:
        st.error("❌ API key not found. Please set MEMO_API_KEY in your .env file.")
    elif not book_title:
        st.warning("⚠️ Please enter a book title.")
    else:
        st.session_state.messages.append({"role": "user", "content": user_query})

        payload = {
            "inputs": {
                "book_title": book_title,
                "Genre": Genre
            },
            "query": user_query,
            "response_mode": "blocking",
            "conversation_id": None,
            "user": "streamlit_user"
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(API_ENDPOINT, headers=headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                assistant_reply = result.get("answer", "(No answer received)")
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            else:
                st.error(f"API error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")

# ---- Display chat history ----
for msg in st.session_state.messages:
    role = "🧑 You" if msg["role"] == "user" else "🤖 Memo AI"
    st.markdown(f"**{role}:** {msg['content']}")
