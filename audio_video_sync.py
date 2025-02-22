import fal_client



# Replace with your own FAL API endpoint

def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])

result = fal_client.subscribe(
    "fal-ai/sync-lipsync",
    arguments={
        "video_url": "output.mp4",
        "audio_url": "ElevenLabs_2025-02-22T02_23_02_Gigi_pre_s50_sb75_se0_b_m2.mp3",
    },
    with_logs=True,
    on_queue_update=on_queue_update,
)
print(result)