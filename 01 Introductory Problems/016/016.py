def solve(apples, idx, bucket1, bucket2, n):
    if idx == n:
        return abs(bucket1-bucket2)
    bkt1 = solve(apples, idx+1, bucket1+apples[idx], bucket2, n)
    bkt2 = solve(apples, idx+1, bucket1, bucket2+apples[idx], n)

    return min(bkt1, bkt2)

if __name__=="__main__":
    n = int(input())
    apples = list(map(int, input().split()))
    minimum_difference = solve(apples, 0, 0, 0, n)
    print(minimum_difference)
    exit(0) 