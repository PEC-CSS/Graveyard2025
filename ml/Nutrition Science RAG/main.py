import os
import dotenv
import pickle
import requests
import pandas as pd
import anthropic
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
CORS(app)
dotenv.load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["nutrition_science_rag"]
collection = db["embeddings"]

EXCEL_FILE_PATH = os.path.join(BASE_DIR, "static", "nutrition_data.xlsx")
HTML_FILE_PATH = os.path.join(BASE_DIR, "static", "website_nutritional.html")

def save_embeddings_to_mongo(embeddings_data):
    chunk_size = 5 * 1024 * 1024
    chunks = [embeddings_data[i:i+chunk_size] for i in range(0, len(embeddings_data), chunk_size)]
    collection.delete_many({"type": "excel_embeddings"})
    for i, chunk in enumerate(chunks):
        collection.insert_one({"type": "excel_embeddings", "chunk_number": i, "data": chunk})

def load_embeddings_from_mongo():
    cursor = collection.find({"type": "excel_embeddings"}).sort("chunk_number", 1)
    data = b"".join(chunk["data"] for chunk in cursor)
    return pickle.loads(data) if data else None

def create_excel_embeddings():
    df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')
    rows_as_text = [
        ", ".join([f"{k}: {v}" for k, v in row.dropna().to_dict().items()])
        for _, row in df.iterrows()
    ]
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    embedded_data = embeddings.embed_documents(rows_as_text)
    to_store = pickle.dumps({"rows": rows_as_text, "embeddings": embedded_data})
    save_embeddings_to_mongo(to_store)
    return {"rows": rows_as_text, "embeddings": embedded_data}

def searxng_search(query, instance='https://searx.be'):
    try:
        resp = requests.get(f'{instance}/search', params={'q': query, 'format': 'json'}, timeout=10)
        results = resp.json().get('results', [])[:5]
        return [{'title': r.get('title', ''), 'link': r.get('url', ''), 'snippet': r.get('content', '')} for r in results]
    except:
        return []

embeddings_data = load_embeddings_from_mongo() or create_excel_embeddings()

@app.route('/')
def index():
    return send_from_directory(os.path.join(BASE_DIR, 'static'), 'website_nutritional.html')

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    content = data.get('content', '')

    if not question:
        return jsonify({'error': 'Missing question'}), 400

    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

        context = ""
        if content:
            chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_text(content)
            embedded_chunks = embeddings.embed_documents(chunks)
            best_match_index = max(
                range(len(embedded_chunks)),
                key=lambda i: embeddings.cosine_similarity(embedded_chunks[i], embeddings.embed_query(question)),
            )
            context = chunks[best_match_index]

        best_excel_match_index = max(
            range(len(embeddings_data["embeddings"])),
            key=lambda i: embeddings.cosine_similarity(embeddings_data["embeddings"][i], embeddings.embed_query(question)),
        )
        excel_context = embeddings_data["rows"][best_excel_match_index]

        prompt = f"""
        You are a helpful assistant that answers questions about a website's content and nutritional information.
        Use ONLY the following content to answer the question.
        If the answer cannot be found in the content, respond with 'NO_ANSWER_FOUND'.
        WEBSITE CONTENT:
        {context}
        EXCEL CONTENT:
        {excel_context}
        USER QUESTION: {question}
        Answer the question based only on the information provided.
        """

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}],
        )

        answer = response.content[0].text

        if answer == 'NO_ANSWER_FOUND':
            web_results = searxng_search(question)
            if web_results:
                web_context = "\n".join([
                    f"Title: {r['title']}\nSnippet: {r['snippet']}\nLink: {r['link']}" for r in web_results
                ])
                web_prompt = f"""
                Use the following web search results to answer the question:
                {web_context}

                USER QUESTION: {question}
                Provide a concise and informative answer based on the search results.
                If no relevant information is found, say "I couldn't find definitive information about this topic."
                """
                web_response = client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=500,
                    messages=[{"role": "user", "content": web_prompt}],
                )
                return jsonify({'answer': web_response.content[0].text, 'source': 'web_search', 'web_results': web_results})

            return jsonify({'answer': "I couldn't find information about this topic.", 'source': 'no_source'})

        return jsonify({'answer': answer, 'source': 'local_sources'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs(os.path.join(BASE_DIR, 'static'), exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
