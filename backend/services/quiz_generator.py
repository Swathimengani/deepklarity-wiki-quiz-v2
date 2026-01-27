import os
import json
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


def generate_quiz(title: str, summary: str, sections: list):
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    prompt = PromptTemplate(
        input_variables=["title", "summary", "sections"],
        template="""
You are an expert quiz generator.

Using ONLY the information below, generate a quiz.

TITLE:
{title}

SUMMARY:
{summary}

SECTIONS:
{sections}

RULES:
- Generate 5 to 7 questions
- Each question MUST have:
  - question
  - exactly 4 options
  - correct answer (one of the options)
  - difficulty: easy, medium, or hard
  - short explanation
  - 2–3 related Wikipedia topics
- Do NOT hallucinate facts
- Respond ONLY in valid JSON
- Do NOT include markdown or text outside JSON

JSON FORMAT:
{{
  "quiz": [
    {{
      "question": "",
      "options": ["", "", "", ""],
      "answer": "",
      "difficulty": "easy|medium|hard",
      "explanation": "",
      "related_topics": ["", ""]
    }}
  ]
}}
"""
    )

    response = llm.invoke(
        prompt.format(
            title=title,
            summary=summary,
            sections=", ".join(sections)
        )
    )

    raw_text = response.content.strip()

    try:
        parsed = json.loads(raw_text)
        return parsed["quiz"]
    except Exception:
        raise ValueError("LLM did not return valid JSON")
