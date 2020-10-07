"""
Count the number of prime numbers less than a non-negative number, n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
"""


def countPrimes(n: int) -> int:
    count = 0

    if n < 2:
        return count

    primes_lookup = [True] * n
    primes_lookup[0] = False
    primes_lookup[1] = False

    for i in range(2, len(primes_lookup)):
        if i * i >= n:
            break
        for j in range(i, len(primes_lookup)):
            if i * j >= n:
                break
            primes_lookup[i * j] = False

    for prime in primes_lookup:
        if prime:
            count += 1

    return count


print(countPrimes(10))
print(countPrimes(0))
print(countPrimes(1))
