import streamlit as st
from st_clickable_images import clickable_images
import webbrowser
import base64

# Set Streamlit page title
st.set_page_config(page_title="NORA AI", layout="wide")

st.markdown("""
    <style>
    
           /* Remove blank space at top and bottom */ 
           .block-container {
               padding-top: 0rem;
               padding-bottom: 0rem;
            }
           
    </style>
    """, unsafe_allow_html=True)


def font_to_base64(font_path):
    with open(font_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Path to your font file (ensure this file is in the same directory or update the path)
# Change this to the actual TTF font filename
font_path = "slopes-cufonfonts\\Slopes.ttf"

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
    "<div class='big-font'>NORA <em class='highlight'>AI</em></div>",
    unsafe_allow_html=True
)


def encode_image(image_path, mime_type="image/jpeg"):
    """Encodes an image as a Base64 string."""
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:{mime_type};base64,{encoded}"


# Define local image paths & MIME types
image_files = [
    ("img/SPACE.png", "image/png"),
    ("img/SEA.png", "image/png"),
    ("img/JUNGLE.png", "image/png"),
    ("img/FARM.png", "image/png"),
]

# Encode images
images = [encode_image(file, mime) for file, mime in image_files]

# Display clickable images
clicked = clickable_images(
    images,
    titles=["🌌 Space", "🌊 Sea", "🌳 Jungle", "🌾 Farm"],
    div_style={"display": "flex", "justify-content": "center",
               "flex-wrap": "wrap", "gap": "15px"},
    img_style={"width": "600px", "height": "400px",
               "object-fit": "cover", "border-radius": "10px"},
)


# If an image is clicked, redirect to Eleven Labs AI chat
if clicked == 0:

    # st.video('img\videoplayback.mp4')
    # Redirecting to Eleven Labs
    url = "http://localhost:8502/"
    # url = "https://elevenlabs.io/app/talk-to?agent_id=W3HZWJljPMmSxbtsFoAD"
    # st.markdown(f"[Click here if not redirected]( {url} )", unsafe_allow_html=True)

    # Open in the browser automatically
    webbrowser.open_new_tab(url)

if clicked == 1:

    url = "http://localhost:8503/"
    
    webbrowser.open_new_tab(url)
    
if clicked == 2:
    
    url = "http://localhost:8504/"
    
    webbrowser.open_new_tab(url)
    
if clicked == 3:
    
    url = "http://localhost:8505/"
    
    webbrowser.open_new_tab(url)
