import math

def solve(N, K):
    arr = []
    root = int(math.sqrt(N))
    row = 0
    col = 0
    count = 0
    vec = []
    for i in range(1, N + 1):
        if count > root:
            count = 0
            arr.append(vec)
            vec = []
        vec.append(i)
        count += 1
    if vec:
        arr.append(vec)

    for i in range(N):
        j = K % (N - i)

        while j:
            if col + j < len(arr[row]):
                col += j
                j = 0
            else:
                j -= len(arr[row]) - col
                col = 0
                row += 1
                if row >= len(arr):
                    row = 0

        while len(arr[row]) <= col:
            col = 0
            row += 1
            if row >= len(arr):
                row = 0

        print(arr[row][col], end=" ")
        if i != N - 1:
            del arr[row][col]
            while len(arr[row]) <= col:
                col = 0
                row += 1
                if row >= len(arr):
                    row = 0
    print()

if __name__=="__main__":
    n, k = list(map(int, input().split()))
    solve(n, k)