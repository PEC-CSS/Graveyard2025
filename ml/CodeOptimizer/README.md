Code Optimizer with AI Suggestions and Radon Metrics
This project optimizes Python code by analyzing files using Pylint, automatically formatting them with AutoPEP8, generating AI suggestions with Claude API, and measuring complexity and maintainability using Radon.

🎯 Overview
Analyzes Python code for errors and suggestions using Pylint.

Formats and enhances code readability using AutoPEP8.

Generates optimization suggestions to improve performance, readability, and memory efficiency using Claude API.

Evaluates Cyclomatic Complexity and Maintainability Index before and after optimization using Radon.

🛠️ Tech Stack
Pylint: Code analysis and linting.

AutoPEP8: Automatic code formatting.

Claude API: AI suggestions and improvements.

Radon: Measures Cyclomatic Complexity and Maintainability Index.

Python: Backend with essential libraries.

🚀 How It Works
Load Python Files:
The script scans the data folder for .py files.

Run Pylint Analysis:
Generates a detailed report highlighting potential improvements and issues.

AutoPEP8 Formatting:
Fixes code formatting automatically to meet PEP 8 standards.

Claude API Suggestions:
Sends the code to the Claude API to provide practical suggestions for improving performance and readability.

Measure Code Metrics with Radon:

Cyclomatic Complexity: Indicates the complexity of the code. Lower values are better.

Maintainability Index: Reflects how easy the code is to maintain. Higher values are better.

Compare Metrics Before and After Optimization:
Provides insights into improvements in code complexity and maintainability.

Display Results:

Pylint suggestions.

Optimized code.

Cyclomatic Complexity and Maintainability Index comparison.

AI-generated suggestions and reasoning.

📥 Installation & Setup
Install Required Libraries:

bash
Copy
Edit
pip install -r requirements.txt
Set Up API Key:

Create a .env file in the project directory.

Add your Claude API key:

ini
Copy
Edit
CLAUDE_API_KEY=your_claude_api_key
▶️ Usage
Place Python Files:

Add .py files to the data folder.

Run the Script:

bash
Copy
Edit
python main.py
Check Results:

Pylint suggestions.

Optimized code.

Comparison of Cyclomatic Complexity and Maintainability Index.

AI-generated suggestions and reasoning.

📂 Folder Structure
bash
Copy
Edit
/CodeOptimizer
├── /data
│   ├── file1.py
│   └── file2.py
├── /optimized_code
├── main.py
├── requirements.txt
└── README.md
📊 Code Metrics with Radon
Cyclomatic Complexity (CC):
Measures the number of independent paths through the code.

Lower CC values indicate simpler, more maintainable code.

Higher CC values suggest complex and harder-to-maintain code.

Maintainability Index (MI):
Indicates the ease of maintaining the code.

Higher MI values (closer to 100) suggest better maintainability.

Lower MI values indicate potential difficulty in maintaining the code.

⚙️ Configuration
code_folder - Path to the folder containing code (N:\CodeOptimizer\data).

optd_folder - Path where optimized code is stored.

Claude API key is loaded through .env.