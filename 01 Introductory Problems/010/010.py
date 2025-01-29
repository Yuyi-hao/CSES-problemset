if __name__=="__main__":
    n = int(input())
    curr = 5
    ans = 0
    while curr <= n:
        ans += n//curr
        curr *= 5
    print(ans)
    exit(0)