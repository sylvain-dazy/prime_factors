def prime_factors_of(n: int) -> list:
    factors = []
    if n > 1:
        factors.append(n)
    return factors


def test_prime_factors():
    assert prime_factors_of(1) == []
    assert prime_factors_of(2) == [2]
    assert prime_factors_of(3) == [3]
