# **Local AI Chatbot**  
A **PDF-based question-answering system** that uses **local embeddings and Claude API** to create a personalized knowledge base.

## **Overview**
This project creates a chatbot that can answer questions based on information stored in your PDF documents. It works by:
1. **Reading and extracting text** from PDF files in a specified folder.
2. **Creating vector embeddings** from the text using a local model.
3. **Finding relevant information** when you ask questions.
4. **Using Claude AI** to generate natural language answers based on the retrieved context.

## **Features**
- 📄 **Local Text Processing**: Extracts and processes text from PDF files stored on your computer.  
- 🧠 **Local Vector Embeddings**: Uses HuggingFace's lightweight `"sentence-transformers/all-MiniLM-L6-v2"` model to create embeddings **without sending your data to external services**.  
- ⚡ **Efficient Retrieval**: Employs **FAISS (Facebook AI Similarity Search)** for fast similarity search.  
- 🗣️ **Natural Language Responses**: Leverages **Claude API** to generate helpful, human-like answers.  
- 🔄 **Fallback Mechanism**: Automatically tries alternative Claude models if the primary model is unavailable.  

## **Requirements**
- **Python 3.x**
- **Anthropic API key**
- **Required Python packages**:  
  - `anthropic`
  - `PyPDF2`
  - `langchain-community`
  - `langchain-text-splitters`
  - `faiss-cpu` *(or `faiss-gpu` for GPU acceleration)*
  - `sentence-transformers`

## **Installation**
1. **Clone this repository** or download the code.  
2. **Install the required packages** using:  
   ```sh
   pip install anthropic PyPDF2 langchain-community langchain-text-splitters faiss-cpu sentence-transformers
   ```
3. **Replace the placeholder API key** with your actual Claude API key.  
4. **Ensure your PDF files** are placed in the correct folder (`data`).  

## **Configuration**
### **API Key**  
Replace the placeholder API key with your own in `chatbot.py`:  
```python
# Line 10: Replace with your actual Claude API key
CLAUDE_API_KEY = "your-actual-api-key-here"
```
Get your API key by signing up at **[Anthropic's website](https://www.anthropic.com/)**.

### **PDF File Location**  
Change the PDF folder path in `chatbot.py`:  
```python
# Line 14: Change this path to your own PDF folder location
pdf_folder = r"C:\Your\Path\To\PDFs"  
```
Make sure to:  
✅ Use raw strings (`r"..."`) to avoid issues with backslashes on Windows.  
✅ Create this folder if it doesn't exist.  
✅ Place your **PDF files** in this folder before running the script.  

### **Customize Chunk Size**  
Modify document splitting settings in `chatbot.py`:  
```python
# Line 30: Adjust these values based on your needs
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
```
- 🔹 Increase `chunk_size` for **longer contexts** (e.g., `1000`).  
- 🔹 Increase `chunk_overlap` for **better continuity** between chunks (e.g., `100`).  

### **Change Embedding Model**  
Modify the embedding model in `chatbot.py`:  
```python
# Line 34: Change to another sentence-transformer model if needed
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```
**Options:**  
- `all-MiniLM-L6-v2` *(default, fast but less accurate)*  
- `all-mpnet-base-v2` *(more accurate but slower and larger)*  
- `paraphrase-multilingual-MiniLM-L12-v2` *(for non-English documents)*  

## **Usage**
1. **Place your PDF documents** in the configured `data` folder.  
2. **Run the chatbot script** using:  
3. The chatbot will **load and process all PDF files** in the specified folder.  
4. **Ask questions** about the content of your documents.  
5. Type **`exit`** to quit the chatbot.  

---
**🚀 Enjoy your personalized Local AI Chatbot!**  
