def prime_factors_of(n: int) -> list[int]:
    factors = []
    prime = 2
    while n > 1:
        while n % prime == 0:
            factors.append(prime)
            n /= prime
        prime += 1
    if n > 1:
        factors.append(n)
    return factors


def test_prime_factors():
    assert prime_factors_of(1) == []
    assert prime_factors_of(2) == [2]
    assert prime_factors_of(3) == [3]
    assert prime_factors_of(4) == [2, 2]
    assert prime_factors_of(5) == [5]
    assert prime_factors_of(6) == [2, 3]
    assert prime_factors_of(7) == [7]
    assert prime_factors_of(8) == [2, 2, 2]
    assert prime_factors_of(9) == [3, 3]
