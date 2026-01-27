from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base, WikiQuiz
from services.scraper import scrape_wikipedia
from services.quiz_generator import generate_quiz
import crud

app = FastAPI()

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- DB INIT --------------------
Base.metadata.create_all(bind=engine)

# -------------------- SCRAPE & SAVE --------------------
@app.get("/scrape-and-save")
def scrape_and_save(url: str, db: Session = Depends(get_db)):
    existing = crud.get_quiz_by_url(db, url)
    if existing:
        return {
            "message": "URL already exists",
            "id": existing.id,
            "title": existing.title,
        }

    scraped = scrape_wikipedia(url)
    if "error" in scraped:
        raise HTTPException(status_code=400, detail=scraped["error"])

    quiz = crud.create_wiki_quiz(
        db=db,
        url=url,
        title=scraped["title"],
        summary=scraped["summary"],
        sections=scraped["sections"],
    )

    return {
        "message": "Saved successfully",
        "id": quiz.id,
        "title": quiz.title,
    }

# -------------------- GENERATE QUIZ --------------------
@app.get("/generate-quiz")
def generate_quiz_api(url: str, db: Session = Depends(get_db)):
    quiz_record = crud.get_quiz_by_url(db, url)

    # If not scraped yet → scrape & save FIRST
    if not quiz_record:
        scraped = scrape_wikipedia(url)
        if "error" in scraped:
            raise HTTPException(status_code=400, detail=scraped["error"])

        quiz_record = crud.create_wiki_quiz(
            db=db,
            url=url,
            title=scraped["title"],
            summary=scraped["summary"],
            sections=scraped["sections"],
        )

    # If quiz already generated → reuse it (CACHE)
    if quiz_record.quiz_data:
        return {
            "id": quiz_record.id,
            "title": quiz_record.title,
            "quiz": quiz_record.quiz_data,
        }

    # Generate quiz using stored article data
    quiz_data = generate_quiz(
        title=quiz_record.title,
        summary=quiz_record.summary,
        sections=quiz_record.extracted_data.get("sections", []),
    )

    # Save generated quiz
    quiz_record.quiz_data = quiz_data
    db.commit()
    db.refresh(quiz_record)

    return {
        "id": quiz_record.id,
        "title": quiz_record.title,
        "quiz": quiz_record.quiz_data,
    }

# -------------------- HISTORY --------------------
@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    quizzes = db.query(WikiQuiz).order_by(WikiQuiz.created_at.desc()).all()
    return [
        {
            "id": q.id,
            "url": q.url,
            "title": q.title,
            "created_at": q.created_at,
        }
        for q in quizzes
    ]

# -------------------- QUIZ DETAILS --------------------
@app.get("/quiz/{quiz_id}")
def get_quiz_details(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(WikiQuiz).filter(WikiQuiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return {
        "id": quiz.id,
        "url": quiz.url,
        "title": quiz.title,
        "summary": quiz.summary,
        "sections": quiz.extracted_data.get("sections", []),
        "quiz": quiz.quiz_data,
        "created_at": quiz.created_at,
    }
