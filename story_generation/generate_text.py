from openai import OpenAI
import os

client = OpenAI()

 # Use OpenAI Client

def generate_text(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return completion.choices[0].message.content

