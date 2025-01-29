def get_ways(k):
    ways = 0
    cells = k*k
    middle_cells = (k-4)*(k-4)
    if k == 1:
        ways = 0
    elif k == 2:
        ways += (cells)*(cells-1)
    elif k == 3:
        ways += (cells-3)*(cells-1)
        ways += 8
    else:
        ways += (4)*(cells-3) # corner
        ways += (8)*(cells-4) # beside corner
        ways += ((k-3)*4)*(cells-5) # two cells after corner
        ways += ((k-4)*4)*(cells-7) # middle cells in second row 
        ways += (middle_cells)*(cells-9)
    return ways
if __name__=="__main__":
    n = int(input())
    for k in range(1, n+1):
        ways = get_ways(k)
        print(ways//2)
    exit(0)