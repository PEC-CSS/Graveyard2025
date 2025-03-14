import os
import anthropic
import wikipedia
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def get_wikipedia_content(query, max_results=3):
    try:
        search_results = wikipedia.search(query, results=max_results)
        if not search_results:
            return [], f"No Wikipedia articles found for '{query}'."

        all_content = []
        processed_pages = []

        for result in search_results:
            try:
                page = wikipedia.page(result, auto_suggest=False)

                if page.title in processed_pages:
                    continue
                
                processed_pages.append(page.title)

                page_info = {
                    "title": page.title,
                    "url": page.url,
                    "content": page.content,
                    "summary": page.summary
                }
                all_content.append(page_info)

            except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError):
                continue

        return all_content, None

    except Exception as e:
        return [], f"Error retrieving Wikipedia content: {str(e)}"

def create_vector_store(articles):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks, metadatas = [], []

    for article in articles:
        article_chunks = splitter.split_text(article["content"])
        for chunk in article_chunks:
            chunks.append(chunk)
            metadatas.append({
                "source": article["title"],
                "url": article["url"]
            })

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(chunks, embeddings, metadatas=metadatas)

    return vector_store

def format_citations(similar_docs, articles):
    citations = []
    context = ""

    for doc in similar_docs:
        context += doc.page_content + " "
        source = doc.metadata.get("source", "Unknown Source")

        article_url = next((article["url"] for article in articles if article["title"] == source), None)

        if article_url:
            citations.append(f"{source}: {article_url}")
        else:
            citations.append(source)

    return context.strip(), citations

# Depending on the availability and to reduce error multiple models are stored so that in case a superior one is not working the user can still access the chatbot.

def get_answer(query, vector_store, articles):
    similar_docs = vector_store.similarity_search(query, k=3)
    context, citations = format_citations(similar_docs, articles)

    prompt = f"""You are a helpful assistant that provides information based on Wikipedia content.

Context from Wikipedia:
{context}

Citations:
{citations}

Question: {query}
"""

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=750,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content, citations
    except Exception as e:
        print(f"Failed with model claude-3-5-sonnet-20240620: {e}")
        try:
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=750,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.content, citations
        except Exception as e:
            print(f"Failed with fallback model: {e}")
            return "Error: Could not get a response from Claude API. Please check your API key and available models.", citations

def wikipedia_chatbot():
    print("Wikipedia RAG Chatbot Ready! Ask me anything (type 'exit' to quit).")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        try:
            print("Searching Wikipedia...")
            articles, error = get_wikipedia_content(user_input)

            if error:
                print("Chatbot:", error)
                continue

            print(f"Found {len(articles)} relevant articles: {', '.join(article['title'] for article in articles)}")
            print("Processing information...")

            vector_store = create_vector_store(articles)
            answer, citations = get_answer(user_input, vector_store, articles)

            print("Chatbot:", answer)
            print("Citations:")
            for citation in citations:
                print(f"- {citation}")

        except Exception as e:
            print(f" Error: {str(e)}")

if __name__ == "__main__":
    wikipedia_chatbot()

