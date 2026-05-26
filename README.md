# 🤖 Multi-Agent AI Research System

A powerful **Multi-Agent AI Research Assistant** built using **LangChain, LangGraph, Groq LLM, and Streamlit**.
This system automates the entire research workflow — from searching information to generating structured reports and critical evaluation.

---

## 🚀 Features

* 🔍 **Search Agent**
  Finds relevant and recent information from the web using Tavily API

* 📄 **Reader Agent**
  Scrapes and extracts clean content from selected URLs

* ✍️ **Writer Agent**
  Generates a structured research report:

  * Introduction
  * Key Findings
  * Conclusion
  * Sources

* 🧠 **Critic Agent**
  Evaluates the report and provides:

  * Score (out of 10)
  * Strengths
  * Areas for Improvement
  * Final Verdict

* 🎨 **Streamlit UI**
  Interactive frontend to input topics and view results step-by-step

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* LangGraph
* Groq API (LLM)
* Tavily API (Search)
* BeautifulSoup (Web Scraping)

---

## 📁 Project Structure

```
MULTI AGENT SYSTEM/
│── app.py               # Streamlit UI
│── agents.py            # Agents (Search, Reader, Writer, Critic)
│── tools.py             # Web search & scraping tools
│── pipeline.py          # Workflow logic
│── requirements.txt     # Dependencies
│── .env                 # API keys (not pushed)
│── .gitignore           # Ignore unnecessary files
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-ai.git
cd multi-agent-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows**

```bash
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file and add:

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

### Steps:

1. Push code to GitHub
2. Go to: https://share.streamlit.io
3. Click **New App**
4. Select your repo
5. Choose:

   ```
   app.py
   ```
6. Add secrets:

   ```
   GROQ_API_KEY=xxxx
   TAVILY_API_KEY=xxxx
   ```
7. Deploy 🚀

---

## ⚠️ Known Issues & Fixes

### ❌ Rate Limit Error (Groq)

* Cause: Free tier token limit exceeded
* Fix:

  * Wait for reset
  * Use smaller model:

    ```
    llama-3.1-8b-instant
    ```

---

### ❌ Connection Error (Tavily / Requests)

* Cause: Network timeout or API issue
* Fix:

  * Add try/except in tools.py
  * Retry request
  * Check internet connection

---

### ❌ Tool Call Error

* Cause: Model calling wrong tool (e.g., brave_search)
* Fix:

  * Restrict tools explicitly in agents

---

## 💡 Example Topics to Try

* "Latest advancements in quantum computing 2025"
* "Impact of generative AI on software development"
* "Recent IPL 2026 match analysis"
* "Future of multi-agent AI systems"

---

## 📌 Future Improvements

* Add memory to agents
* Improve UI with charts
* Add multi-source validation
* Use vector database for better retrieval

---

## 👨‍💻 Author

**Riya Priyadarsani Sahu**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

