# 🤖 Django Text To Code Generator Using OpenAI

A Django-based web application that converts natural language text into working code using the OpenAI API. This project demonstrates the power of AI in automating code generation and helping developers quickly transform ideas into functional code snippets.

---

## 📌 Overview

This project allows users to input a text description (prompt), and the system generates corresponding code using OpenAI’s language model. It is built with Django and integrates OpenAI API for intelligent code generation.

It is useful for:

* Developers learning AI integration
* Rapid prototyping
* Understanding prompt-based code generation
* Educational purposes in AI + Web Development

---

## 🚀 Features

* 🧠 Convert text prompts into code using OpenAI API
* 🌐 Web-based interface using Django
* ⚡ Fast and real-time response generation
* 💻 Supports multiple programming outputs (based on prompt)
* 🔐 Secure API key handling
* 📄 Clean and simple UI for user interaction

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **AI Integration:** OpenAI API
* **Frontend:** HTML, CSS, Bootstrap
* **Language:** Python

---

## 📂 Project Structure

```text id="v8q1kd"
Django-Text-To-Code-Generator-Using-OPENAI/
│── app/
│── templates/
│── static/
│── db.sqlite3
│── manage.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash id="k3m9pa"
git clone https://github.com/pratikyadav0205/Django-Text-To-Code-Generator-Using-OPENAI.git
cd Django-Text-To-Code-Generator-Using-OPENAI
```

---

### 2️⃣ Create Virtual Environment

```bash id="x7d0sj"
python -m venv venv
```

---

### 3️⃣ Activate Environment

```bash id="q2l8vn"
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash id="h1p5zc"
pip install -r requirements.txt
```

---

### 5️⃣ Add OpenAI API Key

Create a `.env` file or set environment variable:

```text id="n9v2kd"
OPENAI_API_KEY=your_api_key_here
```

---

### 6️⃣ Run Migrations

```bash id="c4t8xq"
python manage.py migrate
```

---

### 7️⃣ Start Server

```bash id="r6m1wy"
python manage.py runserver
```

---

### 8️⃣ Open in Browser

```text id="z8k2la"
http://127.0.0.1:8000/
```

---

## 💡 How It Works

1. User enters a text prompt (e.g., "Write a Python function to reverse a string")
2. Django sends the prompt to OpenAI API
3. OpenAI generates code based on the input
4. Output is displayed on the web page

---

## 📈 Future Improvements

* Add multiple language selection (Python, JS, Java, C++)
* Improve UI/UX design
* Add user authentication
* Save generated code history
* Deploy on cloud (AWS / Render / Vercel)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Pratik Yadav**
ICT Student & Developer
Interested in Web Development, AI, and Ethical Hacking

---

## ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub!
