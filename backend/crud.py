from sqlalchemy.orm import Session
from models import WikiQuiz


def get_quiz_by_url(db: Session, url: str):
    return db.query(WikiQuiz).filter(WikiQuiz.url == url).first()


def create_wiki_quiz(db: Session, url: str, title: str, summary: str, sections: list):
    quiz = WikiQuiz(
        url=url,
        title=title,
        summary=summary,
        extracted_data={
            "sections": sections
        }
    )
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz


def save_generated_quiz(db: Session, quiz_id: int, quiz_data: list):
    quiz = db.query(WikiQuiz).filter(WikiQuiz.id == quiz_id).first()
    quiz.quiz_data = quiz_data
    db.commit()
    db.refresh(quiz)
    return quiz
