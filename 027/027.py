if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    max_sum = -float('inf')
    total = 0

    for num in nums:
        total += num
        max_sum= max(total, max_sum)

        if total < 0:
            total = 0
    
    print(max_sum)
    exit(0)