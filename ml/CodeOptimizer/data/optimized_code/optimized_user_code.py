import numpy as np

# Constants
SMALL_THRESHOLD = 100
MEDIUM_THRESHOLD = 50
TINY_THRESHOLD = 20

def calculate_a_b(x, y):
    if x > 10:
        a = sum(i * x for i in range(10))
        b = sum(j * y for j in range(5))
    else:
        a = sum(i * j * x for i in range(5) for j in range(5))
        b = sum(i + j for i in range(5) for j in range(5) if j % 2 == 0)
    return a, b

def categorize_result(value, thresholds, categories):
    for threshold, category in zip(thresholds, categories):
        if value > threshold:
            return category
    return categories[-1]

def my_function(x, y):
    a, b = calculate_a_b(x, y)
    
    a_category = categorize_result(a, [SMALL_THRESHOLD], ["big", "small"])
    b_category = categorize_result(b, [MEDIUM_THRESHOLD, TINY_THRESHOLD], ["big", "medium", "tiny"])
    
    print(f"Result A is {a_category}")
    print(f"Result B is {b_category}")
    
    result = a + b
    print(f"The final result is: {result}")
    print(f"Result is {'even' if result % 2 == 0 else 'odd'}")

# Example usage
my_function(12, 5)