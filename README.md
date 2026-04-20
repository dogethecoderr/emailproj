# 📧 Email Prioritization App

## 🎯 Why this project

In schools, counselors and support staff are often overwhelmed by large volumes of emails from students, parents, and teachers. Important requests—such as urgent academic support, mental health concerns, or administrative issues—can easily get buried in general or low-priority messages.

Email overload is a common problem beyond schools as well—important messages often get buried under low-priority or spam-like content. This project was created to address that by building a simple, fast, and local email prioritization dashboard that helps users quickly identify what matters most.

The goal is to reduce time wasted sorting through inbox clutter by automatically (or semi-automatically) categorizing emails into priority levels, making it easier to focus on urgent and important communication first.

---

A lightweight Flask-based email prioritization dashboard that helps users quickly identify and manage important emails through a clean, responsive interface.

---

## 🚀 Overview

This project is designed to simplify email management by categorizing and prioritizing incoming messages. It provides a minimal web interface built with Flask and HTML/CSS, focusing on clarity, speed, and usability.

---

## ✨ Features

* 📬 Email inbox dashboard
* ⭐ Priority-based email tagging (High / Medium / Low)
* 🧠 Simple rule-based or logic-driven sorting (extendable)
* 🌙 Dark mode toggle (UI enhancement)
* ⚡ Lightweight Flask backend
* 🎨 Clean, responsive frontend design

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript

---

## 📁 Project Structure

```
emailproj/
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Main UI
├── static/
│   ├── styles.css          # Styling
│   └── script.js           # Frontend logic (dark mode, etc.)
├── data/
│   └── emails.json         # Sample email dataset (optional)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/dogethecoderr/emailproj.git
cd emailproj
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the app

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 🌙 Dark Mode

The UI includes a dark mode toggle for better usability at night. Preferences can be stored using localStorage (if enabled in JS).

---

## 📌 Future Improvements

* 🔐 User authentication (login system)
* 📡 Gmail / Outlook API integration
* 🧠 AI-based email prioritization
* 🗂️ Database storage (SQLite/PostgreSQL)
* 📱 Mobile-first responsive redesign
* 🔔 Email notifications & alerts

---

## 👨‍💻 Authors

Built by @dogethecoderr and @InfLight1
