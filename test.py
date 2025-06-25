def count_primes(n: int) -> int:
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i : n+1 : i] = [False] * len(range(i*i, n+1, i))
    return sum(sieve)

# Example usage
if __name__ == "__main__":
    import time
    start = time.time()
    total_primes = count_primes(10_000_000)
    print(f"Total primes: {total_primes}")
    print(f"Execution time: {time.time() - start:.2f} seconds")
