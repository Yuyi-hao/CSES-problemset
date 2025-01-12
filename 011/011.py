memo = {}
def can_empty_pile(a, b):
    return not ((2 * a - b) % 3 != 0 or (2 * a - b) < 0 or (2 * b - a) % 3 != 0 or (2 * b - a) < 0)
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        ans = can_empty_pile(a, b)
        print("YES" if ans else "NO")
    exit(0)