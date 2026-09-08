import sys
input = sys.stdin.readline

# ---- Input ----
def inp():
    """Single integer on the line."""
    return int(input())

def inlt():
    """Line of space-separated integers -> list of ints."""
    return list(map(int, input().split()))

def invr():
    """Line of space-separated integers -> lazy map (single-use, good for unpacking)."""
    return map(int, input().split())

def insr():
    """Line as a single token (no internal spaces) -> list of characters."""
    return list(input().rstrip('\n'))

def instr():
    """Line as-is -> raw string, newline stripped, nothing else touched."""
    return input().rstrip('\n')

def inslt():
    """Line of space-separated words -> list of strings (not converted to int)."""
    return input().rstrip('\n').split()

def in2d(n):
    """n lines of space-separated ints -> list of lists (e.g. a matrix)."""
    return [inlt() for _ in range(n)]

def in2dstr(n):
    """n lines of raw strings -> list of strings (e.g. a character grid/maze)."""
    return [instr() for _ in range(n)]

# ---- Output (interactive problems only) ----
def out(x):
    """Single value, flushed immediately."""
    print(x, flush=True)

def outlt(lst):
    """List of values -> space-separated line, flushed immediately."""
    print(' '.join(map(str, lst)), flush=True)

def outmt(*args):
    """Multiple values -> space-separated line, flushed immediately."""
    print(*args, flush=True)
