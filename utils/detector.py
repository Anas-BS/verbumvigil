import json
import os
import re
from pathlib import Path

# Try to import Gemini libraries
try:
    import google.generativeai as genai
    print("Gemini AI SDK loaded successfully!")
except ImportError:
    print("Gemini AI SDK not found. Installing required library...")
    os.system("pip install google-generativeai")
    try:
        import google.generativeai as genai
        print("Gemini AI SDK installed successfully!")
    except ImportError:
        print("Failed to install Gemini AI SDK. API features will be disabled.")
        genai = None

def load_idioms():
    """Load idioms from JSON file."""
    idioms_path = Path(__file__).parent.parent / 'idioms.json'
    if not idioms_path.exists():
        # Return an empty list if file doesn't exist
        return []
    
    with open(idioms_path, 'r') as f:
        return json.load(f)

def detect_cultural_mismatches(text):
    """
    Detect culturally sensitive expressions in the provided text.
    Uses both local idiom database and Gemini AI if available.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        list: Dictionaries containing phrase, explanation, and suggestion
    """
    results = []
    
    # Method 1: Local pattern matching with idioms database
    idioms = load_idioms()
    text_lower = text.lower()
    
    for idiom in idioms:
        phrase = idiom.get('phrase', '').lower()
        if phrase and phrase in text_lower:
            results.append({
                'phrase': phrase,
                'explanation': idiom.get('explanation', 'This may be culturally sensitive.'),
                'suggestion': idiom.get('suggestion', 'Consider rephrasing.'),
                'source': 'local'
            })

    # Method 2: Use Gemini AI for deeper analysis if available
    if genai and os.environ.get("GOOGLE_API_KEY"):
        api_results = analyze_with_gemini(text)
        if api_results:
            for item in api_results:
                # Add source to distinguish from local detections
                item['source'] = 'gemini'
                results.append(item)
            
    return results

def analyze_with_gemini(text):
    """
    Use Gemini AI to detect cultural mismatches.
    
    Args:
        text (str): Text to analyze
        
    Returns:
        list: Detected cultural mismatches
    """
    if not genai:
        return []
    
    try:
        # Configure the Gemini API
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        
        # Use Gemini-2.5 model
        model = genai.GenerativeModel('gemini-2.5')
        
        prompt = f"""
        Analyze the following text for culturally sensitive expressions, idioms, or metaphors 
        that might be confusing or inappropriate when translated to other cultures:

        TEXT: {text}

        For each problematic phrase you find, provide:
        1. The exact phrase from the text
        2. A brief explanation of why it could be problematic
        3. A suggestion for improvement

        Format your response as a JSON array of objects with these keys:
        'phrase', 'explanation', 'suggestion'

        If you don't find any issues, return an empty array.
        """
        
        response = model.generate_content(prompt)
        
        # Process the response to extract the JSON
        try:
            # Extract JSON from response
            content = response.text
            # Find JSON array pattern between square brackets
            json_match = re.search(r'\[\s*\{.*\}\s*\]', content, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                return json.loads(json_str)
            return []
        except Exception:
            # Fallback if JSON parsing fails
            return []
            
    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return []
