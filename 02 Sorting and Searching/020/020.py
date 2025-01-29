if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    prev = nums[0]
    ans = 1
    for i in range(1, n):
        ans += 1 if nums[i-1] != nums[i] else 0
    print(ans)
    exit(0)