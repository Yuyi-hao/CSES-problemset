if __name__=="__main__":
    n = int(input())
    arr = [0]*n
    curr = 2
    idx = 0
    while curr < n+1 and idx < n:
        arr[idx] = curr
        curr += 2
        idx += 1

    curr = 1
    while idx < n and curr < n+1:
        arr[idx] = curr
        curr += 2
        idx += 1

    for i in range(n-1):
        if abs(arr[i]-arr[i+1]) == 1:
            print("NO SOLUTION")
            exit(0)
    print(" ".join([str(i) for i in arr]))
    exit(0)