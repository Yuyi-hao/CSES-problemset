if __name__=="__main__":
    n = int(input())
    nums = [int(i) for i in  input().split()]
    ans = 0
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            ans += abs(nums[i]-nums[i-1])
            nums[i] = nums[i-1]
    
    print(ans)
    exit(0)
