if __name__=="__main__":
    n, max_weight = list(map(int, input().split()))
    weight_list = list(map(int, input().split()))
    weight_list.sort()
    low = 0
    high = n-1
    gondola = 0
    while low <= high:
        weight = weight_list[low]+weight_list[high]
        if weight <= max_weight:
            low += 1
        gondola += 1 
        high -= 1
    
    print(gondola)
    exit(0)