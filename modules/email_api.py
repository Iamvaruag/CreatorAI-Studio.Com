import os
import resend 
from dotenv import load_dotenv

load_dotenv()

def send_script_email(to_email: str, topic: str, content: str) -> dict:
    """
    Sends the generated content package to an email address using the Resend API.
    """
    api_key = os.getenv("RESEND_API_KEY")
    if not api_key:
        return {"success": False, "error": "RESEND_API_KEY is missing in your environment variables."}
    
    resend.api_key = api_key

    html_content = f"""
    <h2>🎬 CreatorAI-Studio Content Package</h2>
    <p><b>Topic / Concept:</b> {topic}</p>
    <hr>
    <div>{content.replace(chr(10), '<br>')}</div>
    <hr>
    <p style="color: gray; font-size: 12px;">Generated automatically via CreatorAI-Studio.</p>
    """

    params = {
        "from": "CreatorAI Studio <onboarding@resend.dev>",
        "to": [to_email],
        "subject": f"🎬 Script Package: {topic[:30]}...",
        "html": html_content,
    }

    try:
        response = resend.Emails.send(params)
        return {"success": True, "data": response}
    except Exception as e:
        return {"success": False, "error": str(e)}