import os
import openai
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def record_audio(filename):
    """
    Records audio from the microphone until the user stops it and saves it as a WAV file.
    
    :param filename: Name of the output WAV file
    """
    fs = 44100  # Sampling frequency
    recording = []
    
    with st.spinner("Recording... Press 'Stop Recording' to stop."):
        stream = sd.InputStream(samplerate=fs, channels=1, dtype='int16')
        stream.start()
        while not st.session_state.get("stop_recording", False):
            frame, _ = stream.read(1024)
            recording.append(frame)
        stream.stop()
    
    recording = np.concatenate(recording, axis=0)
    write(filename, fs, recording)
    st.success(f"Recording saved as {filename}")

def transcribe_audio(filename):
    """
    Transcribes the given audio file using OpenAI's Whisper API.
    
    :param filename: Path to the audio file
    :return: Transcribed text
    """
    with open(filename, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text

# Streamlit UI
st.title("Speech-to-Text Recorder")

if "stop_recording" not in st.session_state:
    st.session_state["stop_recording"] = False

audio_filename = "recorded_audio.wav"

if st.button("Start Recording"):
    st.session_state["stop_recording"] = False
    record_audio(audio_filename)

if st.button("Stop Recording"):
    st.session_state["stop_recording"] = True
    st.success("Recording stopped. You can now transcribe.")

if st.button("Transcribe Audio"):
    start_time = time.time()
    transcription = transcribe_audio(audio_filename)
    end_time = time.time()
    
    time_taken = round(end_time - start_time, 2)
    st.write(f"**Transcription Time:** {time_taken} secs")
    st.write("**Transcription:**")
    st.write(transcription)
