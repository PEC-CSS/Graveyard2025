import os
import io
import anthropic
import pylint.lint
import autopep8
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from contextlib import redirect_stdout

load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

code_folder = r"N:\CodeOptimizer\data"
optimized_folder = os.path.join(code_folder, "optimized_code")
os.makedirs(optimized_folder, exist_ok=True)


def load_code_files(folder):
    code_files = {}
    for file in os.listdir(folder):
        if file.endswith(".py"):
            file_path = os.path.join(folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                code_files[file] = f.read()
    return code_files


def run_pylint(code, file_name):
    temp_file = os.path.join(optimized_folder, f"temp_{file_name}")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(code)
    pylint_output = io.StringIO()
    with redirect_stdout(pylint_output):
        pylint_args = [temp_file, "--output-format=text"]
        pylint.lint.Run(pylint_args, exit=False)
    os.remove(temp_file)
    return pylint_output.getvalue()


def get_claude_optimization(code):
    prompt = f"""
    You are an expert code optimizer.
    Analyze the following Python code and provide suggestions to improve it in terms of:
    - Performance
    - Readability
    - Reducing redundancy
    - Memory efficiency
    Suggest only meaningful and practical improvements with all details and also provide the full optimised code at the end...

    CODE:
    {code}
    """
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        return f"Error calling Claude API: {e}"


def process_code(code_folder):
    code_files = load_code_files(code_folder)
    if not code_files:
        print("No code files found in the folder.")
        return
    for file_name, code in code_files.items():
        print(f"Processing: {file_name}")
        pylint_results = run_pylint(code, file_name)
        if pylint_results.strip():
            print("Pylint Suggestions:")
            print(pylint_results)
        else:
            print("No Suggestion!")
        optimized_code = autopep8.fix_code(code)
        print("Optimized Code:")
        print(optimized_code)
        claude_results = get_claude_optimization(code)
        print("Claude Suggestions:")
        print(claude_results)

process_code(code_folder)