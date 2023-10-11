from prime_factors import prime_factors_of


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
    assert prime_factors_of(2 * 3 * 3 * 5 * 7 * 7 * 7 * 7 * 11 * 13) == [2, 3, 3, 5, 7, 7, 7, 7, 11, 13]
