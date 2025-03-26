import os
import io
import anthropic
import pylint.lint
import autopep8
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from dotenv import load_dotenv
from contextlib import redirect_stdout
import re

load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

code_folder = r"N:\CodeOptimizer\data"
optd_folder = os.path.join(code_folder, "optimized_code")
os.makedirs(optd_folder, exist_ok=True)


def load_code_files(folder):
    code_files = {}
    for file in os.listdir(folder):
        if file.endswith(".py"):
            file_path = os.path.join(folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                code_files[file] = f.read()
    return code_files


def run_pylint(code, file_name):
    temp_file = os.path.join(optd_folder, f"temp_{file_name}")
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(code)
    pylint_output = io.StringIO()
    with redirect_stdout(pylint_output):
        pylint_args = [temp_file, "--output-format=text"]
        pylint.lint.Run(pylint_args, exit=False)
    os.remove(temp_file)
    return pylint_output.getvalue()


def claude_opt(code):
    prompt = f"""
    You are an expert code optimizer.
    Analyze the following Python code and provide suggestions to improve it in terms of:
    - Performance
    - Readability
    - Reducing redundancy
    - Memory efficiency
    Provide the fully optimized code at the end in a code block.
    CODE:
    {code}
    """
    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception as e:
        return f"Error calling Claude API: {e}"


def extract_code_from_claude(response_text):
    match = re.search(r"```python\n(.*?)\n```", response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return response_text.strip()


def calc_metrics(code):
    complexity_results = cc_visit(code)
    cyclomatic_complexity = sum(block.complexity for block in complexity_results)
    maint_after_metrics = mi_visit(code, True)
    return cyclomatic_complexity, maint_after_metrics


def process_code(code_folder):
    code_files = load_code_files(code_folder)
    if not code_files:
        return
    for file_name, code in code_files.items():
        pylint_results_before = run_pylint(code, file_name)
        cyclomatic_before, maint_before_metrics = calc_metrics(code)
        claude_response = claude_opt(code)
        optimized_code = extract_code_from_claude(claude_response)
        if optimized_code == code:
            optimized_code = autopep8.fix_code(code)
        cyclomatic_after, maint_after_metrics = calc_metrics(optimized_code)
        optimized_file_path = os.path.join(optd_folder, f"optimized_{file_name}")
        with open(optimized_file_path, "w", encoding="utf-8") as f:
            f.write(optimized_code)

        print(f"Pylint Suggestions (Before Optimization):\n{pylint_results_before}")
        print(f"Optimized Code:\n{optimized_code}")
        print(f"Comparison of Metrics:")
        print(f"- Cyclomatic Complexity Before: {cyclomatic_before}, After: {cyclomatic_after}")
        print(f"- Maintainability Index Before: {maint_before_metrics}, After: {maint_after_metrics}")
        print(f"Claude Reasoning:\n{claude_response}")

process_code(code_folder)