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

## 🚀 Getting Started

### 🛠 Prerequisites
- Python 3.10+
- PostgreSQL
- Node.js & npm
- Git

---

## 📦 Backend Setup

```bash
cd backend

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

Create .env file (DO NOT COMMIT)

DATABASE_URL=postgresql://username:password@localhost:5432/wikiquiz
GROQ_API_KEY=your_api_key_here

Run backend

uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000

🧑‍💻 Frontend Setup
cd frontend

Install dependencies
npm install

Start frontend
npm run dev


Frontend runs at:

http://127.0.0.1:5173

📡 API Endpoints
Method	Endpoint	Description
GET	/scrape-and-save?url=	Scrape & store Wikipedia data
GET	/generate-quiz?url=	Generate quiz from URL
GET	/history	Fetch quiz history
GET	/quiz/{id}	Get full quiz details
🛡 Environment Variables

The .env file must not be pushed to GitHub.

Add this to .gitignore:

.env

🎨 UI Overview
🧩 Tab 1 – Generate Quiz

Paste Wikipedia URL

Click Generate Quiz

View structured quiz with:

Difficulty badges

Answers & explanations

Related topics

📜 Tab 2 – History

List of past quizzes

Click Details to open quiz modal

🧪 Optional Enhancements

Take Quiz mode (answers hidden)

Question shuffling

User authentication

Deployment (Render / Railway / Vercel)

📜 License

MIT License

🙌 Author

Swathi Mengani
GitHub: https://github.com/Swathimengani

Built with ❤️ using FastAPI & React