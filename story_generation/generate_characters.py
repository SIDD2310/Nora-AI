import fal_client

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

def generate_characters(character, scenario, story_context, child_input):
    text = f"{story_context} {child_input}"
    character_name = character
    result = fal_client.subscribe(
        "fal-ai/flux/dev",
        arguments={
            "prompt": "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
        },
        with_logs=True,
        on_queue_update=on_queue_update,
    )
    return result