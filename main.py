import streamlit as st
from st_clickable_images import clickable_images
import webbrowser

# Set Streamlit page title
st.set_page_config(page_title="Clickable Images Example")

# List of images
images = [
    "https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=2650&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1530053969600-caed2596d242?q=80&w=2574&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1541959833400-049d37f98ccd?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1591797442444-039f23ddcc14?w=700",

]

# Titles for the images
titles = [f"Image #{i}" for i in range(len(images))]

# Display clickable images
clicked = clickable_images(
    images,
    titles=titles,
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

# If an image is clicked, redirect to Eleven Labs AI chat
if clicked > -1:
    
    # Redirecting to Eleven Labs
    url = "https://elevenlabs.io/app/talk-to?agent_id=W3HZWJljPMmSxbtsFoAD"
    st.markdown(f"[Click here if not redirected]( {url} )", unsafe_allow_html=True)
    
    # Open in the browser automatically
    webbrowser.open_new_tab(url)
