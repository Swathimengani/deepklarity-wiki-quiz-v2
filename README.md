# 🧠 Wiki Quiz Generator

A modern full-stack application that transforms Wikipedia articles into interactive, AI-powered quizzes with intelligent difficulty assessment and comprehensive explanations.

---

## ✨ Key Features

### 📚 Intelligent Quiz Generation
- **Smart Content Extraction**: Paste any Wikipedia URL to automatically extract article structure
- **AI-Powered Questions**: Generates contextually relevant multiple-choice questions
- **Difficulty Classification**: Automatic labeling (Easy/Medium/Hard) based on content complexity
- **Detailed Explanations**: Each answer includes educational context
- **Topic Discovery**: Suggests related Wikipedia articles for deeper learning

### 💾 Persistent Storage
- PostgreSQL database for reliable data storage
- Duplicate URL prevention
- Complete quiz history with instant access
- Efficient data retrieval and caching

### 🎯 User Experience
- **Dual Interface**: Separate tabs for quiz generation and history review
- **Modal-Based Details**: Expandable quiz viewer without page navigation
- **Visual Difficulty Indicators**: Color-coded badges for quick scanning
- **Responsive Design**: Seamless experience across devices

---

## 🛠️ Technology Stack

### Backend
- **FastAPI** – High-performance Python web framework
- **SQLAlchemy** – SQL toolkit and ORM
- **PostgreSQL** – Robust relational database
- **BeautifulSoup** – Wikipedia content scraping
- **Groq API** – AI-powered quiz generation

### Frontend
- **React 18** with **Vite** – Fast, modern UI framework
- **Tailwind CSS** – Utility-first styling
- **Fetch API** – Asynchronous data handling
- **Component-Based Architecture** – Reusable, maintainable code

---

## 📁 Project Architecture
```
deepklarity-wiki-quiz/
├── backend/
│   ├── main.py                 # FastAPI application entry
│   ├── database.py             # Database configuration
│   ├── models.py               # SQLAlchemy models
│   ├── crud.py                 # Database operations
│   ├── services/
│   │   ├── scraper.py          # Wikipedia extraction
│   │   └── quiz_generator.py  # AI quiz generation
│   └── requirements.txt        # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx             # Main application component
│   │   ├── main.jsx            # React entry point
│   │   └── components/         # Reusable UI components
│   ├── index.html
│   ├── tailwind.config.js
│   └── package.json
│
├── .gitignore
└── README.md
```

---

## 🚀 Installation & Setup

### Prerequisites
- **Python** 3.10 or higher
- **PostgreSQL** 12 or higher
- **Node.js** 18+ and npm
- **Git** for version control

### 1️⃣ Backend Configuration
```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
cat > .env << EOF
DATABASE_URL=postgresql://username:password@localhost:5432/wikiquiz
GROQ_API_KEY=your_groq_api_key_here
EOF

# Start the server
uvicorn main:app --reload
```

**Backend runs at:** `http://127.0.0.1:8000`

### 2️⃣ Frontend Configuration
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

**Frontend runs at:** `http://127.0.0.1:5173`

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/scrape-and-save?url=` | Scrape Wikipedia and store content |
| `GET` | `/generate-quiz?url=` | Generate quiz from Wikipedia URL |
| `GET` | `/history` | Retrieve all quiz history |
| `GET` | `/quiz/{id}` | Fetch specific quiz details |

---

## 🔒 Security & Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory (never commit this file):
```env
DATABASE_URL=postgresql://username:password@localhost:5432/wikiquiz
GROQ_API_KEY=your_api_key_here
```

### .gitignore Configuration

Ensure your `.gitignore` includes:
```
# Environment files
.env
.env.local

# Python
__pycache__/
*.py[cod]
venv/

# Node
node_modules/
dist/
```

---

## 🎨 Application Interface

### Generate Quiz Tab
1. Paste any Wikipedia URL into the input field
2. Click **Generate Quiz** to process the article
3. View the generated quiz with:
   - Color-coded difficulty badges
   - Multiple-choice options (A–D)
   - Correct answers highlighted
   - Detailed explanations
   - Related topic suggestions

### History Tab
- Browse all previously generated quizzes
- Click **Details** to view full quiz in a modal
- Consistent layout and styling across all quizzes

---

## 🚀 Future Enhancements

- [ ] **Interactive Quiz Mode** – Hide answers for self-testing
- [ ] **Question Shuffling** – Randomize order for repeated practice
- [ ] **User Authentication** – Personal quiz collections
- [ ] **Export Functionality** – PDF/JSON quiz downloads
- [ ] **Deployment** – Render, Railway, or Vercel hosting
- [ ] **Quiz Analytics** – Track performance and topics

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Swathi Mengani**  
GitHub: [@Swathimengani](https://github.com/Swathimengani)

---

<div align="center">

**Built with ❤️ using FastAPI, React, and AI**

</div>