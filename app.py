import streamlit as st
import os
from dotenv import load_dotenv
from modules.script_gen import generate_content_package
from modules.email_api import send_script_email

load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="CreatorAI-Studio | Script Factory",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 CreatorAI-Studio: Content & Script Factory")
st.markdown("Transform raw ideas into viral video hooks, structured scripts, and platform-ready metadata instantly.")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key_input = st.text_input("Gemini API Key", type="password", help="Overrides .env file if provided.")
    if api_key_input:
        os.environ["GEMINI_API_KEY"] = api_key_input
        
    resend_key_input = st.text_input("Resend API Key", type="password", help="For emailing generated scripts.")
    if resend_key_input:
        os.environ["RESEND_API_KEY"] = resend_key_input
    
    st.divider()
    st.markdown("### Output Settings")
    platform = st.selectbox(
        "Target Platform", 
        ["YouTube Shorts / Reels", "YouTube Long-form", "Instagram Caption / Post", "Tech / Dev Blog"]
    )
    tone = st.selectbox(
        "Content Tone", 
        ["Energetic & Hype", "Professional & Technical", "Casual & Relatable", "Cinematic & Narrative"]
    )

# Main Two-Column Workspace
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Input Concept")
    topic = st.text_area(
        "What is your content about?", 
        placeholder="e.g., Building a futuristic esports tournament platform called Valor Arena...", 
        height=180
    )
    generate_btn = st.button("Generate Content Package 🚀", type="primary")

with col2:
    st.subheader("✨ Generated Output")
    
    # Store output in session state so it persists across UI interactions
    if "latest_content" not in st.session_state:
        st.session_state.latest_content = ""
    if "latest_topic" not in st.session_state:
        st.session_state.latest_topic = ""

    if generate_btn:
        if not topic.strip():
            st.warning("Please enter a topic or concept first!")
        else:
            with st.spinner("Crafting your viral content package..."):
                result = generate_content_package(topic, platform, tone)
                
                if result["success"]:
                    st.session_state.latest_content = result["content"]
                    st.session_state.latest_topic = topic
                    st.markdown(result["content"])
                    st.success("✨ Content package generated successfully!")
                else:
                    st.error(f"Error generating content: {result['error']}")
    elif st.session_state.latest_content:
        st.markdown(st.session_state.latest_content)
    else:
        st.info("Enter your concept on the left and click **Generate Content Package** to start building.")

    # Email Dispatch Section (Appears after content is generated)
    if st.session_state.latest_content:
        st.divider()
        st.subheader("📧 Email Script to Inbox")
        recipient_email = st.text_input("Recipient Email Address", placeholder="you@example.com")
        if st.button("Send via Resend API 📨"):
            if not recipient_email.strip():
                st.warning("Please enter a valid email address.")
            else:
                with st.spinner("Sending email..."):
                    email_result = send_script_email(recipient_email, st.session_state.latest_topic, st.session_state.latest_content)
                    if email_result["success"]:
                        st.success(f"Successfully emailed script to {recipient_email}!")
                    else:
                        st.error(f"Failed to send email: {email_result['error']}")