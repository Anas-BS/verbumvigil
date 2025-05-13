# VerbumVigil

A cultural mismatch detector for translators - helps identify culturally sensitive expressions, idioms, or metaphors that may be misunderstood or inappropriate in certain cultures.

## Features

- Detects culturally sensitive idioms and expressions in text
- Provides explanations for why certain phrases may cause issues
- Suggests alternative phrasing options
- Combines both a local idiom database and Gemini 2.5 AI analysis

## Gemini API Integration

The application is integrated with Google's Gemini 2.5 API for enhanced detection capabilities:

- Pre-configured with an API key (AIzaSyALmJ9bWmoOeKoB7gkvat9dePnPUWW2zGc)
- Combines local pattern matching with AI-powered detection
- Results from Gemini API are marked distinctly in the interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/verbumvigil.git
cd verbumvigil
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. The Gemini 2.5 API key is already configured in the app.py file.

## Usage

1. Run the Flask application:
```bash
python app.py
```

2. Open a web browser and navigate to:
```
http://localhost:5000
```

3. Enter the text you want to analyze in the form and click "Analyze Text"

## Project Structure

```
verbumvigil/
│
├── app.py              # Flask backend logic
├── templates/
│   └── index.html      # HTML form and output
├── static/
│   └── style.css       # UI styling
├── utils/
│   └── detector.py     # Phrase detection logic
├── idioms.json         # Idioms and suggestions
├── requirements.txt    # Python dependencies
└── README.md           # Project description
```

## License

MIT
