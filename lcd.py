def LeastCommonMultiple():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    x, y = a, b
    while y:
        x, y = y, x % y
    lcm = abs(a * b) // x if x else 0
    print(lcm)

LeastCommonMultiple()