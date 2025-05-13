from flask import Flask, render_template, request, jsonify
import os
from utils.detector import detect_cultural_mismatches

app = Flask(__name__)

# Gemini API key from environment variable
GEMINI_API_KEY = "AIzaSyALmJ9bWmoOeKoB7gkvat9dePnPUWW2zGc"
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

@app.route('/', methods=['GET'])
def index():
    """Render the input form."""
    return render_template('index.html')

@app.route('/', methods=['POST'])
def analyze():
    """Process the submitted text and return results."""
    text = request.form.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Detect cultural mismatches
    mismatches = detect_cultural_mismatches(text)
    
    # Return results to the template
    return render_template('index.html', 
                          text=text, 
                          mismatches=mismatches,
                          has_results=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
