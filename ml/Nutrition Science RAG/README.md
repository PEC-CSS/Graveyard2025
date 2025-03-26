📚 AI-Powered Nutrition Q&A System with Excel + Web Data + Claude API
This project is a Flask-based AI application that answers nutrition-related questions by combining data from:

Excel File: Nutrition data is embedded into a vector database.
Website Content: Content is dynamically embedded for quick searches.
Claude API: Provides responses based on combined data or general knowledge when required.


✨ Unique Features

🔥 Hybrid Search with Priority:

First checks Excel data.
If no match, checks website content.
Falls back to Claude's general knowledge if necessary.


📊 Excel Data Integration:

Embeds nutrition_data.xlsx into a vector database.
Automatically updates and retrieves results.


🌐 Website Content Embedding:

Splits website content into smaller chunks.
Searches and retrieves the most relevant context for answering questions.


🤖 Claude API for Final Response:

Combines results from Excel, website, and general knowledge.




🚀 How the System Works

Excel Embeddings Creation:

Reads nutrition_data.xlsx and converts rows to text.
Generates embeddings using HuggingFace's all-MiniLM-L6-v2.
Saves embeddings to MongoDB.


Handling Incoming Questions:

Receives a question and content from the API.
Splits content and generates embeddings for similarity search.
Retrieves the most relevant context from:

📊 Excel Data
🌐 Website Content




Claude API Interaction:

Creates a structured prompt combining extracted content.
Sends the prompt to Claude API for generating a response.




📡 API Usage
1. /api/ask

Method: POST
Description: Accepts a question and content, then returns an AI-generated answer.
Request Format:

jsonCopy{
  "question": "What is the nutritional value of spinach?",
  "content": "Optional website content to search"
}

Response Format:

jsonCopy{
  "answer": "Spinach is rich in vitamins A, C, and K, and contains iron and calcium.",
  "source": "local_sources" // or "web_search"
}

📖 Usage Instructions
1. Prerequisites

Python 3.9+
MongoDB running locally or with a connection string

2. Clone the Repository
bashCopygit clone https://github.com/your-username/nutrition-qa-system.git
cd nutrition-qa-system
3. Set Up Environment

Create a virtual environment (optional but recommended):

bashCopypython -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install required Python packages:

bashCopypip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the root directory:

CopyCLAUDE_API_KEY=your_claude_api_key_here
MONGO_URI=your_mongodb_connection_string  # Optional, defaults to localhost
5. Prepare Data Files
