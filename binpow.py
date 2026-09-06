def myPow(x: float, n: int) -> float:
    po = {}
    if n < 0:
        x = 1 / x
        n = -n
    po[0] = 1
    po[1] = x
    def rec(n):
        _p = po.get(n, None)
        if _p is None:
            if n % 2 == 0:
                po[n] = rec(n // 2) * rec(n // 2)
            else:
                i = 0
                __p = 1
                nn = n
                while nn:
                    a = n & (1 << i)
                    if a:
                        __p *= rec(a)
                    i += 1
                    nn >>= 1
                po[n] = __p
        return po[n]
    return rec(n)
