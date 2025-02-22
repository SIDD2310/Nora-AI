import streamlit as st
import openai
from elevenlabs import generate, save, set_api_key
import os

# ========== SET UP API KEYS ==========
openai.api_key = "YOUR_OPENAI_API_KEY"
set_api_key("YOUR_ELEVENLABS_API_KEY")

# ========== HELPER FUNCTIONS ==========

def multi_character_story(child_input, scenario, story_context):
    """
    This function simulates multiple AI characters responding in one go.
    We define separate 'system' messages for each character's persona,
    then combine them into one prompt for a single LLM call.
    """
    
    # Example multi-character prompt. Each character has a short "system" style text.
    # We'll weave them into a single prompt. You can refine to your liking.
    prompt = f"""
    You are a storytelling AI that produces output for three characters, each labeled with their name.
    The story is aimed at children aged 3-5. Keep the language very simple, fun, and positive.

    SCENARIO: {scenario}

    CHARACTERS:
    1) EXPLORER: A friendly, curious leader (like Dora). Speaks in short, upbeat sentences. Often asks the child for help.
    2) SIDEKICK: A playful companion (like a small animal or friend). Often reacts with excitement and sound effects.
    3) HELPER: A wise local character or object in the scenario that offers clues or interesting facts (like an owl, farm animal, or alien).

    IMPORTANT:
    - Use short sentences.
    - Incorporate scenario-appropriate vocabulary to help expand the child's word bank.
    - After narrating a short continuation of the story, end with a direct question to the child so they can respond.
    - Keep it whimsical and encouraging.

    Story context so far: {story_context}
    Child just said: "{child_input}"

    Now produce a short narrative (about 3-5 sentences total). 
    Each sentence should be labeled with the character's name at the start, for example:
    EXPLORER: "Hello there!"
    SIDEKICK: "Wow, that's cool!"
    HELPER: "Let me show you the way."

    End with a question from the EXPLORER to the child.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    story_output = response.choices[0].text.strip()
    return story_output

def text_to_speech(text, voice="Rachel", filename="output.mp3"):
    """
    Convert the text into speech using ElevenLabs and save as an MP3.
    Streamlit can then display an audio player for the MP3.
    """
    audio = generate(
        text=text,
        voice=voice,
        model="eleven_monolingual_v1"
    )
    save(audio, filename)
    return filename

# ========== STREAMLIT APP ==========

def main():
    st.title("Dora-Like Story Companion")
    st.write("Choose an adventure and chat with your AI friends!")
    
    # Use session_state to keep track of scenario, story context, etc.
    if "story_context" not in st.session_state:
        st.session_state.story_context = ""
    if "scenario" not in st.session_state:
        st.session_state.scenario = None
    if "last_output" not in st.session_state:
        st.session_state.last_output = ""

    # ========== SCENARIO SELECTION ==========

    # Display scenario options as buttons with images/icons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Farm"):
            st.session_state.scenario = "Farm"
            st.session_state.story_context = "We arrive at a sunny farm, with cows, chickens, and a big red barn."
    with col2:
        if st.button("Space"):
            st.session_state.scenario = "Space"
            st.session_state.story_context = "We blast off in a rocket, zooming through the stars to explore planets and meteors."
    with col3:
        if st.button("Jungle"):
            st.session_state.scenario = "Jungle"
            st.session_state.story_context = "We trek through thick green trees, hearing monkeys, parrots, and roaring waterfalls."

    # Show current scenario
    if st.session_state.scenario:
        st.subheader(f"Current Scenario: {st.session_state.scenario}")
    else:
        st.info("Please select a scenario to start your adventure.")

    # ========== USER INPUT + STORY GENERATION ==========

    if st.session_state.scenario:
        user_input = st.text_input("Your turn! (Type what the child might say)", "")
        if st.button("Continue the Story"):
            if user_input.strip():
                # Generate story
                story_part = multi_character_story(
                    child_input=user_input,
                    scenario=st.session_state.scenario,
                    story_context=st.session_state.story_context
                )
                
                # Update story context
                st.session_state.story_context += f"\nCHILD: {user_input}\n{story_part}\n"
                st.session_state.last_output = story_part
                
                # Convert to speech
                filename = text_to_speech(story_part, voice="Rachel", filename="story_response.mp3")
                
                # Display the text output
                st.write("**AI Story Response:**")
                st.write(story_part)
                
                # Streamlit audio player
                audio_file = open(filename, 'rb')
                st.audio(audio_file.read(), format='audio/mp3')
                audio_file.close()
            else:
                st.warning("Please type something for the child to say.")
        
        if st.session_state.last_output:
            st.write("---")
            st.write("**Story so far:**")
            st.write(st.session_state.story_context)

    st.write("---")
    st.write("**Tip:** You can pick a new scenario anytime to start a fresh story!")

if __name__ == "__main__":
    main()
