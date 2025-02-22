import streamlit as st
import streamlit.components.v1 as components
from elevenlabs import ElevenLabs
from dotenv import load_dotenv
import os
import base64

st.set_page_config(page_title="Clickable Images Example", layout="wide")

def font_to_base64(font_path):
    with open(font_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Path to your font file (ensure this file is in the same directory or update the path)
# Change this to the actual TTF font filename
font_path = "slopes-cufonfonts\Slopes.ttf"

# Convert the font to Base64
font_base64 = font_to_base64(font_path)

# Inject CSS with the Base64-encoded font
custom_css = f"""
<style>
@font-face {{
    font-family: 'CustomSlopes';
    src: url(data:font/truetype;charset=utf-8;base64,{font_base64}) format('truetype');
}}

.big-font {{
    font-family: 'CustomSlopes', sans-serif;
    font-size: 130px;
    text-align: center;
}}

.highlight {{
    color: #238636;
}}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Display the text using the custom font
st.markdown(
    "<div class='big-font'>SPACE EXPLORATION</div>",
    unsafe_allow_html=True
)
k1, k2, k3 = st.columns([1.5,5,1])
with k2:
    st.image('img\space.jpg', width=1000)


load_dotenv()


html_code = """
<elevenlabs-convai agent-id="qsKlG3E6972vH2w5omkZ"></elevenlabs-convai>
<script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
"""

c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns(9)
# Embed the HTML in Streamlit
with c8:
    components.html(html_code, width=500, height=200)

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
)
# Fetch conversation
response = client.conversational_ai.get_conversation(
    conversation_id="0SafKm1TNSFzHnyrttXO",
)

# Print transcript in a readable format
st.write("Conversation Transcript:\n")
for entry in response.transcript:
    role = "Agent" if entry.role == "agent" else "User"
    st.write(f"{role}: {entry.message}\n")