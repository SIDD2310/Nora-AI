import fal_client




def on_queue_update(update):
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
           print(log["message"])


def lipsync(audio_filename, video_filename):
    result = fal_client.subscribe(
        "fal-ai/sync-lipsync",
         #"fal-ai/latentsync",
        arguments={
            "video_url": video_filename,
            "audio_url": audio_filename,
            "sync_mode":'loop',
        },
        
        with_logs=True,
        on_queue_update=on_queue_update,
    )
    
    return result


