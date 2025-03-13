# Wikipedia RAG Chatbot

## Description
The Wikipedia RAG Chatbot retrieves and summarizes answers from Wikipedia dynamically using Retrieval-Augmented Generation (RAG). The system queries Wikipedia, stores relevant articles, and provides context-aware responses with citations.

## Features
- Fetches Wikipedia articles based on user queries.
- Converts article content into vector embeddings for retrieval.
- Retrieves and summarizes relevant sections.
- Provides accurate citations from Wikipedia sources.
- Uses multiple Claude API models to ensure reliability.

## Tech Stack
- **Wikipedia API** for fetching article content.
- **Embedding Model:** Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`).
- **Vector Database:** FAISS for efficient similarity search.
- **Backend:** Python with key libraries:
  - `wikipedia` for retrieving articles.
  - `langchain_community.vectorstores.FAISS` for storing embeddings.
  - `langchain_huggingface` for embeddings.
  - `anthropic` for Claude API interactions.

## How It Works
1. The chatbot searches Wikipedia for relevant articles based on the user query.
2. It processes article content into vector embeddings using Hugging Face models.
3. FAISS is used to store and retrieve the most relevant chunks.
4. The chatbot formulates a response using Claude API models, incorporating retrieved content.
5. The response is presented along with Wikipedia citations.

## Installation & Usage
### 1. Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
 pip install anthropic wikipedia langchain_community langchain_huggingface sentence-transformers faiss-cpu
```

### 2. Set Up Claude API Key
Replace `CLAUDE_API_KEY` in the script with your API key:
```python
CLAUDE_API_KEY = "your-api-key"
```

### 3. Run the Chatbot
Execute the script in the terminal:
```sh
 python chatbot.py
```

### 4. Interact with the Chatbot
Once the chatbot starts, enter queries related to Wikipedia topics.
- Type your question and press **Enter**.
- The chatbot will fetch relevant Wikipedia articles, process information, and generate an answer.
- It will display the response along with citations.
- Type `exit` or `bye` to close the chatbot.

### Example Interaction:
```
You: What is quantum computing?
Chatbot: Quantum computing is a type of computation that harnesses quantum mechanics...
Citations:
- Quantum computing: https://en.wikipedia.org/wiki/Quantum_computing
```

## Notes
- If Wikipedia does not return relevant articles, the chatbot will inform the user.
- The chatbot uses multiple Claude models to ensure responses even if a model fails.
- Ensure an active internet connection for Wikipedia queries and API calls.
