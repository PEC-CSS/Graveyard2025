import os
import time
import anthropic
import dotenv
from pygooglenews import GoogleNews
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

dotenv.load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def scrape_article(url):
    driver = get_driver()
    try:
        driver.get(url)
        time.sleep(3)
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        article_text = "\n".join([p.text for p in paragraphs])
        driver.quit()
        return article_text
    except Exception as e:
        driver.quit()
        return f"Error: {e}"

gn = GoogleNews()
newstype = input("Enter the Category or Search Term: ")
print("FETCHING LATEST ARTCILES FOR YOU....................\n Ignore the Dev Tools operation")

search_results = gn.search(newstype)
filename = "news_articles.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"\n\n=== News Articles for: {newstype} ===\n")
    for entry in search_results["entries"][:3]:   
        title, article_url = entry['title'], entry['link']
        file.write(f"\nTitle: {title}\nReal Article Link: {article_url}\nPublished: {entry['published']}\n")
        file.write("\nFull Article:\n" + scrape_article(article_url) + "\n" + "=" * 80 + "\n")

print(f"All articles saved in {filename}")

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def load_news_text(news_file):
    if not os.path.exists(news_file):
        return ""
    with open(news_file, "r", encoding="utf-8") as file:
        return file.read()

news_text = load_news_text(filename)

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(news_text)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_texts(chunks, embeddings)

def retrieve_answer(query):
    similar_docs = db.similarity_search(query, k=10)
    context = " ".join([doc.page_content for doc in similar_docs])

    if not context.strip():
        return "No relevant news found."

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=500,
            messages=[{"role": "user", "content": f"Context: {context} Query: {query}"}],
        )
        return response.content
    except Exception:
        return "Error: Could not get a response from Claude API."

print("News Chatbot Ready! Ask about the latest news (type 'exit' to quit).")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    print("Chatbot:", retrieve_answer(user_input))
