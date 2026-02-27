# 🎭 Character AI Chatbot (Groq + Python)

A simple Python-based chatbot that responds in different **character styles** like a Cowboy 🤠, Philosopher 🧘, or Scientist 🤖 using the Groq API.

---

## 🚀 Features

* 🎭 Multiple character personalities
* 💬 Interactive CLI chat
* 🔐 Secure API key using `.env`
* ⚡ Fast responses using Groq LLMs
* 🧠 Easy to extend with more characters

---

## 🛠️ Tech Stack

* Python
* Groq API
* python-dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
python -m pip install groq python-dotenv
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 🚫 Important (Security)

Make sure `.env` is added to `.gitignore`:

```
.env
```

---

## ▶️ Run the App

```bash
python app.py
```

---

## 🎮 Usage

1. Choose a character:

   * Cowboy 🤠
   * Philosopher 🧘
   * Scientist 🤖

2. Ask any question

3. Get responses in the selected character’s style

---

## 📁 Project Structure

```
project/
│── app.py
│── .env              # ignored
│── .gitignore
│── README.md
│── .env.example
```

---

## 🧠 Example

**Input:**

```
Who are you?
```

**Cowboy Response:**

```
Well partner, I’m just a wanderer ridin’ through the plains of knowledge...
```

**Philosopher Response:**

```
To ask who I am is to question the nature of identity itself...
```

---

## ⚙️ Configuration

You can change the model inside `app.py`:

```python
model="llama-3.1-8b-instant"
```

---

## 🌱 Future Improvements

* 🌐 Web interface (Flask/Streamlit)
* 🧠 Chat memory
* 🔊 Voice output
* 🎭 More characters

---

## 🙌 Acknowledgements

* Groq for fast LLM inference
* Open-source community

---
