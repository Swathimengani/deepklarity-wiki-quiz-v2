# 🧠 Wiki Quiz Generator

A full-stack web application that scrapes Wikipedia articles and generates structured, AI-powered quizzes with difficulty levels, explanations, and related topics.  
Built using **FastAPI**, **PostgreSQL**, **React**, and **Tailwind CSS**.

---

## ✨ Features

### 🔹 Quiz Generation
- Paste any Wikipedia URL
- Automatically extracts:
  - Title
  - Summary
  - Key sections
- Generates a quiz with:
  - Question text
  - Four multiple-choice options (A–D)
  - Correct answer
  - Short explanation
  - Difficulty level (Easy / Medium / Hard)
  - Suggested related Wikipedia topics

### 🔹 Data Persistence
- All scraped and generated data is stored in **PostgreSQL**
- Prevents duplicate URLs
- Reusable quiz history

### 🔹 History & Review
- View all previously generated quizzes
- Click **Details** to open a modal with the full quiz
- Reuses the same structured quiz layout

### 🔹 Clean UI
- Modern, minimal design
- Card-based layout
- Difficulty badges
- Responsive and user-friendly

---

## 🛠️ Tech Stack

### Backend
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- Wikipedia scraping (BeautifulSoup)
- AI-powered quiz generation

### Frontend
- **React (Vite)**
- **Tailwind CSS**
- Fetch API
- Modal-based UI

---

## 📁 Project Structure

deepklarity-wiki-quiz/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── crud.py
│ ├── services/
│ │ ├── scraper.py
│ │ └── quiz_generator.py
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── components/
│ ├── index.html
│ ├── tailwind.config.js
│ └── package.json
│
└── README.md
