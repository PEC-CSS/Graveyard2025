def calculate_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    print(f"The area of the circle is {area}")

def main():
    r = float(input("Enter the radius: "))
    calculate_area(r)

if __name__ == "__main__":
    main()
