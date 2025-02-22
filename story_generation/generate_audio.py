from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
load_dotenv()


client = ElevenLabs()
def generate_audio(prompt):
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="jBpfuIE2acCO8z3wKNLl", # Adam pre-made voice
        output_format="mp3_22050_32",
        text=prompt,
        model_id="eleven_turbo_v2_5", # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )
    # uncomment the line below to play the audio back

    save_file_path = f"{uuid.uuid4()}.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    print(f"{save_file_path}: A new audio file was saved successfully!")

    return save_file_path
