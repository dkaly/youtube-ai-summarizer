# AI YouTube Study Assistant

An AI-powered web application which converts YouTube videos into structured study notes and allows user to ask follow up questions about the video content using conversational memory

---

## Features

- Paste a YouTube video URL
- Automatically extracts video transcript
- Generates structured summaries
- Key ideas + important details 
- AI-powered follow up Q&A (memory-based chat)
- Clean, simple API-ready backend

---

## Tech Stack

- Python
- Flask (API backend)
- OpenAI API
- YouTube Transcript API
- dotenv (environment variables)

---

## How It Works

1. User inputs a YouTube URL  
2. Backend extracts transcript using YouTube Transcript API  
3. Transcript is sent to OpenAI model  
4. AI returns structured study notes  
5. (Future feature) Users can ask follow-up questions about the video

---

## Project Status

Currently running as a backend prototype (CLI + API conversion in progress).

Planned upgrades:
- React frontend UI
- Conversation memory system
- Database storage for chat history
- Deployment to cloud (Render/Vercel)

---

This project is not intended for public deployment due to API cost constraints.
