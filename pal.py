def is_palindrome(n: int) -> bool:
    # Negative numbers are generally not considered palindromes
    if n < 0:
        return False
        
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
        
    return original == reversed_num

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid whole number.")
else:
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")