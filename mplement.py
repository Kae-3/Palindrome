def PrimeSieve(limit: int) -> list[int]:
    """Return all prime numbers less than or equal to limit."""
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for candidate in range(2, int(limit**0.5) + 1):
        if is_prime[candidate]:
            for multiple in range(candidate * candidate, limit + 1, candidate):
                is_prime[multiple] = False

    return [number for number, prime in enumerate(is_prime) if prime]


def LoveYou3000(start: int, end: int) -> list[int]:
    """Return all prime numbers in the inclusive range from start to end."""
    if start > end:
        raise ValueError("start must be less than or equal to end")
    if end < 2:
        return []

    is_prime = [True] * (end - start + 1)
    for candidate in range(2, int(end**0.5) + 1):
        first_multiple = max(candidate * candidate, ((start + candidate - 1) // candidate) * candidate)
        for multiple in range(first_multiple, end + 1, candidate):
            is_prime[multiple - start] = False

    if start <= 1:
        for number in range(start, min(end, 1) + 1):
            is_prime[number - start] = False

    return [number for number in range(start, end + 1) if is_prime[number - start]]


if __name__ == "__main__":
    try:
        lower_bound = int(input("Enter the start of the range: "))
        upper_bound = int(input("Enter the end of the range: "))
        range_primes = LoveYou3000(lower_bound, upper_bound)
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        print(f"Primes up to {upper_bound}: {PrimeSieve(upper_bound)}")
        print(f"Primes from {lower_bound} to {upper_bound}: {range_primes}")