from elevenlabs.client import ElevenLabs
from elevenlabs import play
def sound_effect(prompt):
    client = ElevenLabs()
    audio = client.text_to_sound_effects.convert(text=prompt)
    return audio
