
# 🚀 Code Optimizer with AI Suggestions and Radon Metrics

This project optimizes Python code by analyzing files using **Pylint**, automatically formatting them with **AutoPEP8**, generating AI suggestions with **Claude API**, and measuring complexity and maintainability using **Radon**.

---

## 🎯 Overview
- **Analyzes Python code** for errors and suggestions using Pylint.
- **Formats and enhances code readability** using AutoPEP8.
- **Generates optimization suggestions** to improve performance, readability, and memory efficiency using Claude API.
- **Evaluates Cyclomatic Complexity and Maintainability Index** before and after optimization using Radon.

---

## 🛠️ Tech Stack

| Technology   | Purpose                          |
|--------------|----------------------------------|
| Pylint       | Code analysis and linting        |
| AutoPEP8     | Automatic code formatting        |
| Claude API   | AI suggestions and improvements  |
| Radon        | Code complexity and maintainability |
| Python       | Backend with essential libraries |

---

## 🚀 How It Works

1. **Load Python Files:** The script scans the `/data` folder for `.py` files.
2. **Run Pylint Analysis:** Generates a detailed report highlighting potential improvements and issues.
3. **AutoPEP8 Formatting:** Fixes code formatting automatically to meet PEP 8 standards.
4. **Claude API Suggestions:** Sends the code to the Claude API to provide suggestions for improving performance and readability.
5. **Measure Code Metrics with Radon:**
   - **Cyclomatic Complexity:** Indicates the complexity of the code. Lower values are better.
   - **Maintainability Index:** Reflects how easy the code is to maintain. Higher values are better.
6. **Compare Metrics Before and After Optimization:** Provides insights into improvements in code complexity and maintainability.

---

## 📥 Installation & Setup

### 1. Install Required Libraries:
```bash
pip install -r requirements.txt
```

### 2. Set Up API Key:
- Create a `.env` file in the project directory.
- Add your Claude API key:
```ini
CLAUDE_API_KEY=your_claude_api_key
```

---

## ▶️ Usage

### 1. Place Python Files:
Add `.py` files to the `/data` folder.

### 2. Run the Script:
```bash
python main.py
```

### 3. Check Results:
- **Pylint suggestions**
- **Optimized code**
- **Comparison of Cyclomatic Complexity and Maintainability Index**
- **AI-generated suggestions and reasoning**

---

## 📂 Folder Structure
```bash
/CodeOptimizer
├── /data
│   ├── file1.py
│   └── file2.py
├── /optimized_code
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Code Metrics with Radon

### Cyclomatic Complexity (CC)
- Measures the number of independent paths through the code.
- **Lower CC values:** Simpler and more maintainable code.
- **Higher CC values:** Complex and harder-to-maintain code.

### Maintainability Index (MI)
- Indicates the ease of maintaining the code.
- **Higher MI values (closer to 100):** Better maintainability.
- **Lower MI values:** Potential difficulty in maintaining the code.

---

## ⚙️ Configuration

| Configuration    | Description                                  |
|------------------|----------------------------------------------|
| `code_folder`     | Path to the folder containing code (`N:\CodeOptimizer\data`) |
| `optd_folder`     | Path where optimized code is stored         |
| `CLAUDE_API_KEY`  | API key loaded through `.env`               |

---

