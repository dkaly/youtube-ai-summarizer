from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import urlparse, parse_qs


app = Flask(__name__)
CORS(app)

#load api key
load_dotenv()
client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

@app.route("/")
def home():
    return "YouTube Summarizer AI backend is running"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    url = data["url"]

    #video id
    ###video_id = url.split("v=")[1].split("&")[0] #www.youtube.com/watch?v=  < UF8uR6Z6KLc >  &t=10s
    parsed_url = urlparse(url)
    if "youtube.com" in url:
        video_id = parse_qs(parsed_url.query)["v"][0]
    elif "youtu.be" in url:
        video_id = parsed_url.path[1:]
    else:
        return jsonify({
            "error: Invalid YouTube URL"
        }), 400

    #fetch transcript
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)
    text = " ".join([snippet.text for snippet in transcript])

    #give to ai
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [ {
            "role": "user",
                "content" : f"""
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


    summary = response.choices[0].message.content

    return jsonify({
        "summary": summary
    })

if __name__ == "__main__":  
    app.run(debug = True)


