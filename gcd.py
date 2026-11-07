def find_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
except ValueError:
    print("Please enter valid whole numbers.")
else:
    print(f"The GCD of {first_number} and {second_number} is {find_gcd(first_number, second_number)}.")