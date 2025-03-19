YouTube Transcript Q&A Bot

Description

The YouTube Transcript Q&A Bot allows users to extract transcripts from YouTube videos and retrieve relevant answers based on user queries. It uses Retrieval-Augmented Generation (RAG) to provide context-aware responses.

Features

Fetches YouTube video transcripts automatically.

Stores transcripts for efficient retrieval.

Converts transcript content into vector embeddings for search.

Retrieves and summarizes relevant sections based on user queries.

Uses multiple Claude API models to generate accurate responses.

Tech Stack

YouTube Transcript API for fetching transcripts.

Embedding Model: Hugging Face (sentence-transformers/all-MiniLM-L6-v2).

Vector Database: FAISS for similarity search.

Backend: Python with key libraries:

youtube-transcript-api for transcript retrieval.

langchain_community.vectorstores.FAISS for storing embeddings.

langchain_huggingface for embeddings.

anthropic for Claude API interactions.

How It Works

The bot fetches the YouTube video transcript based on the provided video ID.

It processes the transcript into vector embeddings using a Hugging Face model.

FAISS is used to store and retrieve relevant transcript sections.

The chatbot formulates a response using Claude API models based on retrieved content.

The response is displayed with timestamps from the transcript.