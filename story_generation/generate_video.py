import fal_client

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

def generate_video(character, scenario, story_context):
    generation_prompt = f"""
    Create a cartoonish video of a {character} in a "{scenario}" setting. The video should be cartoonish and not too complicated. This is some extra context of the character: '{story_context}' and should be suitable for a young child. 
    
    Please have the {character} talking to the camera, as to explain something to the young child. 
    """
    result = fal_client.subscribe(
        "fal-ai/hunyuan-video",
        arguments={
            "prompt": generation_prompt,
        },
        with_logs=True,
        on_queue_update=on_queue_update,
    )
    return result
