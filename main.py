import streamlit as st
from st_clickable_images import clickable_images
import webbrowser
import base64

# Set Streamlit page title
st.set_page_config(page_title="Clickable Images Example", layout="wide")

st.markdown("""
    <style>
    
           /* Remove blank space at top and bottom */ 
           .block-container {
               padding-top: 0rem;
               padding-bottom: 0rem;
            }
           
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size:120px !important;
}
</style>
""", unsafe_allow_html=True)

# Custom CSS for "Slopes" font
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Slope&display=swap');

.big-font {
    font-family: 'Slopes', sans-serif;
    font-size: 50px;
    text-align: center;
}

.highlight {
    color: #238636;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Display text with the custom font
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
    ("img/space.avif", "image/avif"),
    ("img/sea.jpg", "image/jpeg"),
    ("img/jungle.jpg", "image/jpeg"),
    ("img/farm.jpg", "image/jpeg"),
]

# Encode images
images = [encode_image(file, mime) for file, mime in image_files]

# Display clickable images
clicked = clickable_images(
    images,
    titles=["🌌 Space", "🌊 Sea", "🌳 Jungle", "🌾 Farm"],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap", "gap": "15px"},
    img_style={"width": "600px", "height": "400px", "object-fit": "cover", "border-radius": "10px"},
)


# If an image is clicked, redirect to Eleven Labs AI chat
if clicked > -1:
    
    # Redirecting to Eleven Labs
    url = "https://elevenlabs.io/app/talk-to?agent_id=W3HZWJljPMmSxbtsFoAD"
    # st.markdown(f"[Click here if not redirected]( {url} )", unsafe_allow_html=True)
    
    # Open in the browser automatically
    webbrowser.open_new_tab(url)
