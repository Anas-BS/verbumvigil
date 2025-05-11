# copilot-instructions.md

## 📌 Project Name: VerbumVigil

VerbumVigil is a Flask-based web application designed to help translators, editors, and writers detect **culturally sensitive expressions, idioms, or metaphors** in translated texts that may be misunderstood or inappropriate in certain cultures.

---

## 🧠 Copilot Objectives

Help the user build a lightweight, clean, and functional **web app** with the following features:

- Accept user input (translated text)
- Analyze the input for culturally risky or confusing expressions
- Flag problematic phrases with explanations and rewrite suggestions
- Present results clearly in the browser (no JS frameworks needed)

---

## 📁 Project Structure

Follow this structure for creating and editing files:

verbumvigil/
│
├── app.py # Flask backend logic
├── templates/
│ └── index.html # HTML form and output
├── static/
│ └── style.css # Optional UI styling
├── utils/
│ └── detector.py # Phrase detection logic
├── idioms.json # Idioms and suggestions
├── copilot-instructions.md # Copilot guidance file
└── README.md # Project description


---

## 🛠️ Languages and Tools to Use

- Python 3 (Flask)
- HTML/CSS
- JSON (for idioms database)
- Regex or keyword search
- Optional NLP libraries (e.g., spaCy) — but only free/open-source ones

Avoid:
- External APIs with costs
- JS frameworks (React, Vue, etc.)
- Heavy ML models unless local and lightweight

---

## 🔧 File-Level Instructions

### `app.py`
- Create Flask routes:
  - `GET /` to render input form
  - `POST /` to receive text and return flagged results
- Call the detection function from `utils/detector.py`
- Pass results to the template via `render_template`

### `utils/detector.py`
- Load `idioms.json`
- Define `detect_cultural_mismatches(text)`:
  - Lowercase and search for idioms in input text
  - Return a list of dicts: phrase, explanation, suggestion

### `idioms.json`
- JSON array of cultural idioms, e.g.:
```json
{
  "phrase": "kick the bucket",
  "explanation": "This idiom means 'to die'. It may be confusing or inappropriate in formal or intercultural contexts.",
  "suggestion": "Use 'passed away' instead."
}

