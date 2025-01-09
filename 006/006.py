def get_spiral_num(row ,col):
    num = 0
    if col <= row:
        if row&1:
            num = ((row-1)*(row-1)) + col
        else:
            num = (row*row) - (col-1)
    else:
        if col&1:
            num = (col*col) - (row-1)
        else:
            num = ((col-1)*(col-1)) + row
    return num

if __name__=="__main__":
    n = int(input().strip())
    for _ in range(n):
        row, col = [int(i) for i in input().strip().split()]
        ans = get_spiral_num(row, col)
        print(ans, end=" ")  
    exit(0)