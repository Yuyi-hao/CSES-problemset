if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    low = 1

    for num in nums:
        if num > low:
            break
        low += num
    print(low)
    exit(0)    

