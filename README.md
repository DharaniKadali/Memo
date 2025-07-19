# 📚 Memo AI – Book Writing Assistant

Memo AI is a lightweight Streamlit application that helps writers, authors, students, and bloggers brainstorm book chapters, outlines, or content ideas using AI. Just enter a topic or chapter title and get AI-generated content instantly.

## 🚀 Features

- ✍️ Input any idea, topic, or chapter title
- 🤖 AI-generated content via Dify.ai API
- 💬 Interactive chat history with the AI
- 🔐 Environment-based API key management
- 🌐 Easily deployable to Streamlit Cloud or Hugging Face Spaces

## 🖼️ Demo

> Coming soon...

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)
- **Backend/API:** Dify.ai `chat-messages` endpoint
- **Environment Variables:** Managed using `python-dotenv`
- **Language:** Python 3.9+

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Memo.git
   cd Memo
````

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root folder and add:

   ```env
   MEMO_API_KEY=your-dify-api-key-here
   MEMO_API_ENDPOINT=https://api.dify.ai/v1/chat-messages
   ```

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

## 🔑 How It Works

* Accepts user input (idea/topic/chapter title)
* Sends input as a query to Dify.ai with the required `"book_title"` field
* Receives AI-generated content and displays it in the interface
* Chat history is preserved within the session

## 📁 Project Structure

```
Memo/
├── app.py                # Main Streamlit app
├── .env                  # API key (not to be committed)
├── requirements.txt      # Python dependencies
├── README.md             # Project overview
```

## ⚠️ Notes

* Make sure your Dify AI app supports the `book_title` input
* If you get a 400 error from the API, ensure required fields like `book_title`, `tone`, or `language` (if enabled) are included

## 👩‍💻 Author

Created by \[Your Name]
[GitHub Profile](https://github.com/DharaniKadali)



