def prime_factors_of(n: int) -> list[int]:
    factors = []
    prime = 2
    while n > 1:
        while n % prime == 0:
            factors.append(prime)
            n /= prime
        prime += 1
    return factors
