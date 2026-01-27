from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class WikiQuiz(Base):
    __tablename__ = "wiki_quizzes"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(String, nullable=False)

    extracted_data = Column(JSON, nullable=False)   # sections, entities, etc
    quiz_data = Column(JSON, nullable=True)         # FULL quiz JSON

    created_at = Column(DateTime, default=datetime.utcnow)
