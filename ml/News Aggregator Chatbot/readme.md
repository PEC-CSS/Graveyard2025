# News Scraper and Chatbot

This project fetches the latest news articles based on a user-defined category or search term, scrapes article content, stores the data, and provides a chatbot interface for querying the stored news using the Claude API.

## How It Works

1. **User Input:** The user provides a news category or search term.
2. **Fetching News:** The script retrieves the latest articles using Google News.
3. **Scraping Content:** Each article's content is scraped using Selenium.
4. **Storing Data:** The articles are saved in a text file.
5. **Vectorization:** The text is split into chunks and converted into embeddings using FAISS.
6. **Chatbot Interaction:** The user can query the news data, and the chatbot retrieves the most relevant articles using FAISS and generates responses with Claude API.

## Installation

To use this project, install the required dependencies:


pip install -r requirements.txt
```

## Usage

1. **Run the script:**
2. **Enter a search term or category** (e.g., "Technology").
3. **Wait for articles to be fetched and scraped.**
4. **Interact with the chatbot** by asking questions about the news.
5. **Type 'exit' to quit the chatbot.**

## Configuration Options

- **Increasing the number of articles:** Change this line in the script:
  ```python
  for entry in search_results["entries"][:3]:  # Change 3 to a higher number
  ```
- **Adjusting internet connection wait time:** Modify the `time.sleep(3)` line in `scrape_article(url)`.
- **Changing chatbot model settings:** Adjust parameters in:
  ```python
  response = client.messages.create(
      model="claude-3-5-sonnet-20240620",
      max_tokens=500,
  ```

## Required Changes Before Running

- **Set up API keys:** Create a `.env` file and add your `CLAUDE_API_KEY`.
- **Ensure ChromeDriver is installed and up to date.**

## Requirements

The `requirements.txt` file contains all dependencies:

```
os
anthropic
dotenv
pygooglenews
selenium
webdriver-manager
langchain_huggingface
langchain_community
langchain_text_splitters
faiss-cpu
sentence-transformers
```

## Notes

- This script runs in **headless mode** using Selenium.
- Ensure **ChromeDriver is compatible** with your Chrome version.
- The chatbot may return **limited results if news articles are insufficient**.

