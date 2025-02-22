from story_generation import generate_characters, generate_video, generate_text, lipsync, generate_audio
from elevenlabs import play
welcome_prompt = """Just like Dora the explorer, Generate a short introduction, introducing a very young kid to this space environment like it is starting out on a journey. 
You are the character called <Sparkles> and are a <Unicorn>
<Sparkles> is a friendly and curious unicorn who loves exploring and learning about the world around him. He has a bright and adventurous spirit and loves to go on adventures.
He is a bit shorter than Dora, but taller than most unicorns. He has a white and brown coat, and his eyes are blue and green. He has a long, curly tail, and his ears are long and sharp.
He is very friendly and loves to play with his friends. He likes to talk about his favorite things, like unicorns and space exploration.
He is very curious and loves to learn new things. He is always asking questions and trying to figure out how things work.
He is very brave and loves to go on adventures. He is always looking for new places to explore and new things to discover.


Write some text that introduces the young child to this environment and to Sparkles. Don't make it too long and make it simple.
"""

character_prompt = "Generate a character that is a young kid, who is curious and adventurous. "
def welcome():
    welcome_text = generate_text.generate_text(welcome_prompt)
    print(welcome_text) #debug
    welcome_voice = generate_audio.generate_audio(welcome_text)
    play(welcome_voice) #debug
    # generate_characters(welcome_text,character_prompt)
    
    # for each in range(3):
    #     character_text = generate_text(character_prompt)
    #     print(character_text)
    #     welcome_voice = generate_audio(character_text)
    #     welcome_video = generate_video("Dora", "space", "Introduction", welcome_text)
    #     lipsync(welcome_video, welcome_voice)
    
    
    

    # print(welcome_video)
    # lipsync(welcome_video)

welcome()

    
    
    

# on click of the image, we generate a video introduction of the storyboard and the scenario
# we then generate the story board for the walktrough
# we then generate the characters for the story board
# we then generate the voice for each character
# we then generate the audio for the story board
# we then generate the video for the story board
# we then generate lipsync for the final video for the 
