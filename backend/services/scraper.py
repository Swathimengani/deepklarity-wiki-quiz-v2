import requests
import re
from bs4 import BeautifulSoup


def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        return {
            "error": f"Failed to fetch page. Status code: {response.status_code}"
        }

    soup = BeautifulSoup(response.text, "html.parser")

    # ---------- TITLE ----------
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No title found"

    # ---------- SUMMARY ----------
    paragraphs = soup.find_all("p")

    raw_summary = " ".join(
        p.get_text(strip=True)
        for p in paragraphs
        if p.get_text(strip=True)
    )

    summary = re.sub(r"\[\d+\]", "", raw_summary)
    summary = summary[:2000]

    # ---------- SECTIONS (ROBUST METHOD) ----------
    sections = []

    for h2 in soup.find_all("h2"):
        text = h2.get_text(separator=" ", strip=True)

        # Remove "[edit]"
        text = re.sub(r"\[edit\]", "", text, flags=re.IGNORECASE).strip()

        if not text:
            continue

        # Skip non-content sections
        if text.lower() in [
            "contents",
            "references",
            "external links",
            "see also",
            "notes",
            "bibliography",
            "further reading"
        ]:
            continue

        sections.append(text)

    return {
        "title": title,
        "summary": summary,
        "sections": sections
    }
