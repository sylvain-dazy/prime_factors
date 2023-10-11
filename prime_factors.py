def prime_factors_of(n: int) -> list[int]:
    factors = []
    if n > 1:
        if n % 2 == 0:
            factors.append(2)
            n /= 2
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
