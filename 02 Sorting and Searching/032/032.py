from collections import defaultdict
def main(n, nums):
    seen = defaultdict(int)
    ans = 0
    left = 0
    for right in range(n):
        if nums[right] in seen and seen[nums[right]] >= left:
            left = seen[nums[right]]+1
        seen[nums[right]] = right
        ans = max(ans, right-left+1)

    return ans
    
if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(main(n, nums))
    exit(0)