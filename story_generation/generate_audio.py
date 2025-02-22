from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

load_dotenv()

def generate_audio(prompt):
    client = ElevenLabs()
    audio = client.text_to_speech.convert(
        text=prompt,
        voice_id="jBpfuIE2acCO8z3wKNLl",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    return audio

