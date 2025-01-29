if __name__=="__main__":
    n, x = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    dct = {}
    if min(nums) > x:
        print('IMPOSSIBLE')
        exit(0)
    for idx, num in enumerate(nums):
        if x-num in dct:
            print(idx+1, dct[x-num])
            exit(0)
        dct[num] = idx+1
    print('IMPOSSIBLE')
    exit(0)