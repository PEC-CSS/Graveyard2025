from bs4 import BeautifulSoup
from langchain_core.documents import Document
from uuid import uuid4
from langchain_cohere import CohereEmbeddings

import os

from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient

load_dotenv()

# Read HTML content from a file
with open('nutrition_website.html', 'r', encoding='utf-8') as file:
    html_cont = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_cont, 'html.parser')

doc = []
# Extract text from all tags
all_tags = soup.find_all("div")
for tag in all_tags:
    doc.append( Document(
    page_content=f"{tag.get_text()}",
    metadata={"source": "tweet"},))

    

cohere_api_key = os.getenv("COHERE_API_KEY")
embeddings_model = CohereEmbeddings(model="embed-english-light-v3.0",cohere_api_key= cohere_api_key )

query = input("Enter you query: ")


# initialize MongoDB python client
MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)

DB_NAME = "langchain_test_db"
COLLECTION_NAME = "langchain_test_vectorstores"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "langchain-test-index-vectorstores"

MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

vector_store = MongoDBAtlasVectorSearch(
    collection=MONGODB_COLLECTION,
    embedding=embeddings_model,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)

# Create vector search index on the collection

vector_store.create_vector_search_index(dimensions=384)




uuids = [str(uuid4()) for _ in range(len(doc))]
vector_store.add_documents(documents=doc, ids=uuids)

retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.5},
)

results = retriever.invoke(query)

if len(results)==0:
    print("Searching web for your answer...")
    from langchain_anthropic import ChatAnthropic
    llm = ChatAnthropic(model="claude-3-7-sonnet-20250219",
    temperature=0,
    max_tokens=1024,
    timeout=None,
    max_retries=2,
     api_key="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",)
    
    result  =llm.invoke(("You are a professional nutrition science assistant . you generate to the point answers (short and concise) relevant to the questions . here is the question :"+ query))

print(result.content)
    


    