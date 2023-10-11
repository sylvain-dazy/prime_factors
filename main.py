from prime_factors import prime_factors_of

if __name__ == '__main__':
    print("Enter a number less than 1 in order to close the application")
    n = int(input("What number do you want to decomposed ? "))
    while n > 1:
        print(f"The decomposition of {n} is {prime_factors_of(n)}")
        n = int(input("What number do you want to decomposed ? "))
