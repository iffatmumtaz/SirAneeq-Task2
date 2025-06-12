# 💬 Gemini Chatbot using LiteLLM + OpenRouter

This is a simple command-line chatbot using Google's Gemini model via OpenRouter and LiteLLM.

---

## 📦 Requirements

- Python 3.10+
- [LiteLLM](https://github.com/BerriAI/litellm)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- An API key from [OpenRouter.ai](https://openrouter.ai/)

---

## ⚙️ Installation

1. **Clone or download this repo.**

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # For Windows
   source venv/bin/activate  # For Linux/Mac
Install required packages:

bash
Copy
Edit
pip install litellm python-dotenv
Create a .env file in the root folder and add your OpenRouter API key:

ini
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_api_key_here
🧠 How It Works
The chatbot uses the Gemini model via LiteLLM and OpenRouter to respond to user input. It runs entirely in your terminal.

▶️ Usage
Simply run the script:

bash
Copy
Edit
python main.py
You'll see:

python
Copy
Edit
💬 Gemini Chatbot started. Type 'exit' to quit.
You:
Type your message and press Enter. To quit, type exit.

🧠 Model Used
google/gemini-2.5-pro-preview-05-06 (via OpenRouter)

You can change the model from the model= argument in the code.

To see supported models: https://openrouter.ai/models

🛠 File Structure
bash
Copy
Edit
project-folder/
│
├── main.py          # The chatbot script
├── .env             # Your API key goes here (not shared publicly!)
└── README.md        # This file
📢 Disclaimer
This is for educational and experimental purposes only. Do not expose your API key publicly.

📬 Credits
LiteLLM

OpenRouter