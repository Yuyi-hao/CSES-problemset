def calculate_stick_length(arr):
    arr.sort()
    median = arr[len(arr) // 2]
    ans = 0

    for length in arr:
        ans += abs(median - length)
    return ans

if __name__=="__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    ans = calculate_stick_length(nums)
    print(ans)
    exit(0)