from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from dotenv import load_dotenv
import os

#load api key
load_dotenv()
client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

#get input
url = input("Paste YouTube URL: ")
#video id
video_id = url.split("v=")[1].split("&")[0] #www.youtube.com/watch?v=  < UF8uR6Z6KLc >  &t=10s
#fetch transcript
ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch(video_id)
text = " ".join([snippet.text for snippet in transcript])

print("\Generating AI Summary:\n")

#give to ai
response = client.chat.completions.create(
    model = "gpt-4.1-mini",
    messages = [ {
        "role": "user",
            content = f"""
            You are an AI assistant that creates structured study notes from YouTube videos.

            Rules:
            - Be concise
            - Do not repeat transcript
            - Use clear headings
            - Use bullet points

            Output format:
            Summary:
            Key Ideas:
            Important Details:

            Transcript:
            {text}
            """ 
            } 
        ]
    )


print(response.choices[0].message.content)