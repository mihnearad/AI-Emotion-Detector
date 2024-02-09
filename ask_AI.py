from openai import OpenAI
import os
from dotenv import load_dotenv
from analyze_webcam import analyze_webcam  # Import the analyze_webcam function
load_dotenv()

#main script to ask OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Replace these lines with your actual code to get age, gender, and emotion from the webcam analysis
age_result, gender_result, emotion_result = analyze_webcam(duration=2)

# Create a user message incorporating the variables
user_message = f"I am a {age_result} year old {gender_result} who's feeling {emotion_result}, say something to me."

system_instruction = "You are a mood improver bot. I am giving you my current state and your goal is to change it. Keep it to 2 sentences."

openai_response = ""  # Initialize an empty string

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_message}
    ],
    stream=True,
)

# Capture the OpenAI response
openai_response = ""
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        openai_response += chunk.choices[0].delta.content

# Print the final OpenAI response
print(openai_response)
