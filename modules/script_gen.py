import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def generate_content_package(topic: str, platform: str, tone: str) -> dict:
    """
    Generates viral hooks, scripts, titles, and tags using google-generativeai.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
    
    prompt = f"""
    You are an expert AI content creator, scriptwriter, and social media strategist.
    Create a high-engagement content package based on these parameters:
    - **Topic / Concept:** {topic}
    - **Target Platform:** {platform}
    - **Tone / Vibe:** {tone}

    Provide the output clearly structured with Markdown headings:
    1. **Viral Hooks** (3 attention-grabbing openers for the first 3 seconds)
    2. **Main Script / Outline** (Engaging script body with pacing and visual cues)
    3. **Catchy Titles** (3 high-CTR title options)
    4. **Tags & Hashtags** (Optimized for search and discovery)
    """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return {"success": True, "content": response.text}
    except Exception as e:
        return {"success": False, "error": str(e)}