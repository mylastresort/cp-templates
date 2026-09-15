def find_primes(start: int, end: int) -> set[int]:
    # this uses O(n log n) time complexity
    # algorithm: find multiples of x greater than x, and exclude them
    # we start by 2, then all following numbers

    ans = set()

    for x in range(max(start, 2), end + 1):
        if any(x % i == 0 for i in ans):
            continue
        ans.add(x)

    return ans

def is_prime(n: int) -> bool:
    ans = set()

    for x in range(2, n + 1):
        if any(x % i == 0 for i in ans):
            continue
        ans.add(x)

    return n in ans

def countPrimes(n: int):
    # counts the number of prime numbers strictly less than n
    # time complexity equal to O(n log n)
    ans = [True] * (max(2, n))
    ans[0] = False
    ans[1] = False
    s = len(ans) - 2

    for x in range(2, n):
        if ans[x] and x * x < n:
            for i in range(x * x, n, x):
                s -= ans[i]
                ans[i] = False
    return s

if __name__ == "__main__":
    n = int(input("Enter number: "))

    primes = is_prime(n)

    print(f"is_prime : {primes}")