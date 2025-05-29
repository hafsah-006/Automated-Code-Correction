def sieve(max):
    primes = []
    is_prime = [True] * (max + 1)  # Initialize a list to mark numbers as prime
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for n in range(2, int(max**0.5) + 1): #optimization: only iterate up to the square root of max
        if is_prime[n]:
            for i in range(n*n, max + 1, n): # Mark multiples of n as not prime, starting from n*n
                is_prime[i] = False

    for n in range(2, max + 1):
        if is_prime[n]:
            primes.append(n)
    return primes
