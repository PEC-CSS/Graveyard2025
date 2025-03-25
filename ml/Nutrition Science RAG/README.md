# 📚 AI-Powered Nutrition Q&A System with Excel + Web Data + Claude API

This project is a **Flask-based AI application** that answers nutrition-related questions by combining data from:  
1. **Excel File:** Nutrition data is embedded into a FAISS vector database.  
2. **Website Content:** Content is dynamically embedded using FAISS for quick searches.  
3. **Claude API:** Provides responses based on combined data or general knowledge when required.  

---

## ✨ **Unique Features**
- 🔥 **Hybrid Search with Priority:**  
   - First checks Excel FAISS data.  
   - If no match, checks website content.  
   - Falls back to Claude’s general knowledge if necessary.  

- 📊 **Excel Data Integration:**  
   - Embeds `nutrition_data.xlsx` into a FAISS vector database.  
   - Automatically updates and retrieves results from FAISS.  

- 🌐 **Website Content Embedding:**  
   - Splits website content into smaller chunks.  
   - Searches and retrieves the most relevant context for answering questions.  

- 🤖 **Claude API for Final Response:**  
   - Combines results from Excel, website, and general knowledge.  

---

## 🚀 **How the System Works**
1. **Excel Embeddings Creation:**  
   - Reads `nutrition_data.xlsx` and converts rows to text.  
   - Generates embeddings using HuggingFace's `all-MiniLM-L6-v2`.  
   - Saves FAISS index to `excel_faiss_index`.  

2. **Handling Incoming Questions:**  
   - Receives a question and content from the API.  
   - Splits content and generates embeddings for similarity search.  
   - Retrieves the most relevant context from:  
      - 📊 Excel Data  
      - 🌐 Website Content  

3. **Claude API Interaction:**  
   - Creates a structured prompt combining extracted content.  
   - Sends the prompt to Claude API for generating a response.  

---

## 📡 **API Usage**

### 1. `/api/ask`
- **Method:** `POST`  
- **Description:** Accepts a question and content, then returns an AI-generated answer.  
- **Request Format:**
```json
{
  "question": "What is the nutritional value of spinach?",
  "content": "Content scraped from a website"
}
```
- **Response Format:**
```json
{
  "answer": "Spinach is rich in vitamins A, C, and K, and contains iron and calcium."
}
```

---

## 📖 **Usage Instructions**

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-repo/ai-nutrition-chatbot.git
cd ai-nutrition-chatbot
```

### 2. **Set Up Environment**
- Install required Python packages:
```bash
pip install -r requirements.txt
```

### 3. **Set API Key for Claude**
- Create a `.env` file in the root directory:
```
CLAUDE_API_KEY=your_claude_api_key_here
```

### 4. **Run the Flask Application**
```bash
python app.py
```
- Access the application at:
```
http://127.0.0.1:5000
```

---

🎉 **Ready to explore AI-powered nutrition answers!** 🎉
