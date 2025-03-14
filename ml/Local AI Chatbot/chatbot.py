import os
import anthropic
import PyPDF2
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Replace with your actual Claude API key
CLAUDE_API_KEY="YOUR API KEY WITH IN THE STRINGS"

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

# This is the folder in which user will store the pdf files that will be generated
pdf_folder = r"N:\Local AI Chatbot\data"  

def load_pdf_text(pdf_folder):
    all_text = ""
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, file)
            with open(pdf_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    all_text += page.extract_text() + " "
    return all_text

pdf_text = load_pdf_text(pdf_folder)

# Text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(pdf_text)

# Vector Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_texts(chunks, embeddings)

def retrieve_answer(query):
    similar_docs = db.similarity_search(query, k=2)
    context = " ".join([doc.page_content for doc in similar_docs])

    # Depending on the availability and to reduce error multiple models are stored so that in case a superior one is not working the user can still access the chatbot.
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=500,
            messages=[{"role": "user", "content": f"Use the following context to answer: {context} Query: {query}"}],
        )
        return response.content
    except Exception as e:
        print(f"Failed with model claude-3-5-sonnet-20240620: {e}")
        try:
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=500,
                messages=[{"role": "user", "content": f"Use the following context to answer: {context} Query: {query}"}],
            )
            return response.content
        except Exception as e:
            print(f"Failed with fallback model: {e}")
            return f"Error: Could not get a response from Claude API. Please check your API key and available models."

print("Chatbot Ready! Ask me anything (type 'exit' to quit).")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        answer = retrieve_answer(user_input)
        print("Chatbot:", answer)
    except Exception as e:
        print(f"Error: {e}")