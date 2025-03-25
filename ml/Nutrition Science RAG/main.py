from flask import Flask, request, jsonify, send_file
import anthropic
import os
import dotenv
import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

app = Flask(__name__)
dotenv.load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

EXCEL_FILE_PATH = "N:/static/nutrition_data.xlsx"
EXCEL_VECTOR_DB_PATH = "N:/static/excel_faiss_index"

def create_excel_embeddings():
    df = pd.read_excel(EXCEL_FILE_PATH, engine='openpyxl')
    rows_as_text = []
    for _, row in df.iterrows():
        row_dict = row.dropna().to_dict()
        row_text = ", ".join([f"{k}: {v}" for k, v in row_dict.items()])
        rows_as_text.append(row_text)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    faiss_db = FAISS.from_texts(rows_as_text, embeddings)
    faiss_db.save_local(EXCEL_VECTOR_DB_PATH)
    return faiss_db

if os.path.exists(EXCEL_VECTOR_DB_PATH):
    faiss_db = FAISS.load_local(
        EXCEL_VECTOR_DB_PATH,
        HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
        allow_dangerous_deserialization=True
    )
else:
    faiss_db = create_excel_embeddings()

@app.route('/')
def index():
    return send_file('N:/static/webiste final nutritional.html')

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    content = data.get('content')
    if not question or not content:
        return jsonify({'error': 'Missing question or content'}), 400
    try:
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(content)
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.from_texts(chunks, embeddings)
        similar_docs = db.similarity_search(question, k=3)
        context = " ".join(doc.page_content for doc in similar_docs)
        excel_results = faiss_db.similarity_search(question, k=3)
        excel_context = " ".join(doc.page_content for doc in excel_results)
        if not context.strip() and excel_context.strip():
            return jsonify({'answer': f"Here is what I found from the Excel data:\n{excel_context}"})
        prompt = f"""
        You are a helpful assistant that answers questions about a website's content and nutritional information.
        Use ONLY the following content to answer the question.
        If the answer cannot be found in the content, say "I don't have information about that from this webpage or the Excel file."
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
        if response and response.content:
            return jsonify({'answer': response.content[0].text})
        else:
            return jsonify({'answer': "I'm not sure how to respond to that based on the content provided."})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'An error occurred while generating the response.'}), 500

if __name__ == '__main__':
    app.run(debug=True)