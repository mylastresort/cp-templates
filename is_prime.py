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

if __name__ == "__main__":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    primes = find_primes(start, end)

    print(f"Prime numbers between {start} and {end}: {primes}")