# Code Optimizer with AI Suggestions

This project optimizes Python code by analyzing files using Pylint, automatically formatting them with AutoPEP8, and providing AI-generated suggestions for improvement through the Claude API.

---

## 🎯 **Overview**

- Analyzes Python code for errors and suggestions using Pylint.
- Formats and enhances code readability using AutoPEP8.
- Generates optimization suggestions to improve performance, readability, and memory efficiency using Claude API.

---

## 🛠️ **Tech Stack**

- **Pylint**: Code analysis and linting.
- **AutoPEP8**: Automatic code formatting.
- **Claude API**: AI suggestions and improvements.
- **FAISS**: Optional for vector storage (imported but not used in the current version).
- **Hugging Face Embeddings**: Prepares embeddings (imported but not used in the current version).
- **Python**: Backend with essential libraries.

---

## 🚀 **How It Works**

1. **Load Python Files:**  
   The script scans the `data` folder for `.py` files.

2. **Run Pylint Analysis:**  
   Generates a detailed report highlighting potential improvements and issues.

3. **AutoPEP8 Formatting:**  
   Fixes code formatting automatically to meet PEP 8 standards.

4. **Claude API Suggestions:**  
   Sends the code to the Claude API to provide practical suggestions for improving performance and readability.

5. **Display Results:**  
   Shows the suggestions, formatted code, and potential optimizations.

---

## 📥 **Installation & Setup**

1. **Install Required Libraries:**
```bash
pip install -r requirements.txt
```

2. **Set Up API Key:**
- Create a `.env` file in the project directory.
- Add your Claude API key:
```
CLAUDE_API_KEY=your_claude_api_key
```

---

## ▶️ **Usage**

1. **Place Python Files:**
   - Add `.py` files to the `data` folder.

2. **Run the Script:**
```bash
python main.py
```

3. **Check Results:**
   - Pylint suggestions.
   - Optimized code.
   - AI-generated suggestions for improvement.

---

## 📂 **Folder Structure**
```
/CodeOptimizer
├── /data
│   ├── user_code.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ **Configuration**

- **`code_folder`** - Path to the folder containing code (`N:\CodeOptimizer\data`).
- **`optimized_folder`** - Path where optimized code is stored.
- Claude API key is loaded through `.env`.

