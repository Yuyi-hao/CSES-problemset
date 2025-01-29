if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 1
    seen = [0]*(n+1)
    seen[0] = 1
    for num in nums:
        if seen[num-1] == 0:
            ans += 1
        seen[num] = 1
    
    print(ans)
    exit(0)