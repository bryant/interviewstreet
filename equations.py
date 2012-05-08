from math import log, factorial
from operator import mul

def prime_sieve(n):
    '''Prime sieve up to and including n'''
    sieve = [False, False] + [True]*(n-1)

    for i in xrange(2, n+1):
        if sieve[i]:
            # below won't work on istreet because earlier versions of py
            # restricted integer args to C longs.
            #for j in xrange(i*i, n+1, i):
            #    sieve[j] = False
            j = i*i
            while j < n+1:
                sieve[j] = False
                j += i

    return sieve

def pf_factorial(n):
    '''Given n, find the prime factorization of n!. Returns
    [(p0, a0), (p1, a1), ...] such that n = p0**a0 * p1**a1 * ...
    '''

    def power_(p_):
        div = p_
        count = 0

        while div <= n:
            count += n / div
            div *= p_

        return count

    primes = [i for i, x in enumerate(prime_sieve(n)) if x]
    factors = [(p, power_(p)) for p in primes if n/p > 0]

    return factors

def prime_factorize(n):
    '''Naively factorize n into its prime constituents.'''
    top = int(n**0.5) + 1
    primes = [i for i, x in enumerate(prime_sieve(top)) if x]

    factors = []

    while n > 1:
        p = primes.pop(0)
        count = 0
        while n % p == 0:
            n /= p
            count += 1

        factors.append((p, count))

    return factors

def test_pff():
    '''Tests pf_factorial.'''
    for i in range(2, 18):
        for x, y in zip(pf_factorial(i), prime_factorize(factorial(i))):
            assert(x == y)

def num_soln(n):
    '''Given n, calculate number of (x, y) such that
    1/x + 1/y = 1/n!

    Let x = n! + k. Then 1/y = 1/n! - 1/(n!+k), or
        y = n! + (n!)**2/k

    So x is always an integer if k is. So y is an integer if k evenly
    divides (n!)**2. So we need to find number of factors of the factorial
    squared.
    '''

    nfac = pf_factorial(n)
    n2fac = [2*a+1 for _, a in nfac]

    numfac = reduce(mul, n2fac)

    return numfac

if __name__ == "__main__":
    from sys import stdin

    N = int(stdin.readline())
    print num_soln(N) % 1000007
