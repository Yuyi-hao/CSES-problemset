if __name__=="__main__":
    n = int(input())
    arr = [0]*n
    for i in input().split():
        arr[int(i)-1] = int(i)
    for idx, val in enumerate(arr):
        if idx != val-1:
            print(idx+1)
            exit(0)
    print(n)
    exit(0)