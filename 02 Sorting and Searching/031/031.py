def solve(n, m, values, swaps):
    values.insert(0, 0)
    res = []
    position = [0] * (n + 1)
    for i in range(1, n + 1):
        position[values[i]] = i
    count = 1
    for i in range(1, n):
        count += position[i] > position[i + 1]
    updated_pairs = set()
    for i in range(m):
        l, r = swaps[i]
        if values[l] + 1 <= n:
            updated_pairs.add((values[l], values[l] + 1))
        if values[l] - 1 >= 1:
            updated_pairs.add((values[l] - 1, values[l]))
        if values[r] + 1 <= n:
            updated_pairs.add((values[r], values[r] + 1))
        if values[r] - 1 >= 1:
            updated_pairs.add((values[r] - 1, values[r]))
        for swapped in updated_pairs:
            count -= position[swapped[0]] > position[swapped[1]]
        values[l], values[r] = values[r], values[l]
        position[values[l]] = l
        position[values[r]] = r
        for swapped in updated_pairs:
            count += position[swapped[0]] > position[swapped[1]]
        res.append(count)
        updated_pairs.clear()
    return res

if __name__=="__main__":
    n, m = tuple(map(int, input().split()))
    nums = list(map(int, input().split()))
    swaps = []
    for _ in range(m):
        swaps.append(list(map(int, input().split())))
    
    res = solve(n, m, nums, swaps)
    for i in res:
        print(i)