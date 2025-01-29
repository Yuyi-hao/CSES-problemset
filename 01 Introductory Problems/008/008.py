if __name__=="__main__":
    n = int(input())
    total = (n*(n+1))//2
    if total&1:
        print("NO")
        exit(0)
    print("YES")
    # first set
    arr = [False]*(n+1)
    compute = total//2
    curr = n
    count = 0
    while compute:
        if compute > curr:
            arr[curr] = True
            compute -= curr
            curr -= 1
        else:
            arr[compute] = True
            compute -= compute
        count += 1
    print(count)
    for i in range(1, n+1):
        if arr[i]:
            print(i, end=" ")
    print()
    print(n-count)

    for i in range(1, n+1):
        if not arr[i]:
            print(i, end=" ")
    print()
    exit(0)