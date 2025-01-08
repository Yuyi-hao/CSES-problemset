if __name__=="__main__":
    sequence = input().strip()
    ans = 1
    curr = 1
    n = len(sequence)
    if n < 1:
        print(0)
        exit(0)
    for idx in range(1, n):
        if sequence[idx] == sequence[idx-1]:
            curr += 1
        else:
            curr = 1
        ans = max(ans, curr)
    print(ans)
    exit(0)