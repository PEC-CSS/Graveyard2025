# Dirty and unoptimized code
def my_function(x, y):
    a = 0
    b = 0
    if x > 10:
        for i in range(10):
            a += i * x
        for j in range(5):
            b += j * y
    elif x <= 10:
        for i in range(5):
            for j in range(5):
                a += i * j * x
                if j % 2 == 0:
                    b += i + j
    else:
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    a += i + j + k
                    b += i * j * k
    if a > 100:
        print("Result A is big")
        if b > 50:
            print("Result B is also big")
        else:
            print("Result B is small")
    else:
        print("Result A is small")
        if b > 20:
            print("Result B is medium")
        else:
            print("Result B is tiny")
    result = a + b
    print(f"The final result is: {result}")
    if result % 2 == 0:
        print("Result is even")
    else:
        print("Result is odd")
my_function(12, 5)
