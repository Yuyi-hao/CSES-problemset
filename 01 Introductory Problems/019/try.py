on_path = [[False]*9 for _ in range(9)]
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
PATH_LENGTH = 48

def solve(org_path, row, col, pos):
    if((on_path[row][col-1] and on_path[row][col+1]) and\
        (not on_path[row-1][col] and not on_path[row+1][col])):
        return 0
    if((on_path[row-1][col] and on_path[row+1][col]) and\
        (not on_path[row][col-1] and not on_path[row][col+1])):
        return 0
    
    if(row==7 and col==1):
        return 1 if pos == PATH_LENGTH else 0
    
    if(pos == PATH_LENGTH):
        return 0
    
    res = 0
    on_path[row][col] = True
    if org_path[pos] == '?':
        for dr, dc in zip(DR, DC):
            nxtR = row+dr
            nxtC = col+dc
            if(not on_path[nxtR][nxtC]):
                res += solve(org_path, nxtR, nxtC, pos+1)
    else:
        if org_path[pos] == 'U':
            dr, dc = -1, 0
        if org_path[pos] == 'D':
            dr, dc = 1, 0
        if org_path[pos] == 'L':
            dr, dc = 0, -1
        if org_path[pos] == 'R':
            dr, dc = 0, 1
        nxtR = row+dr
        nxtC = col+dc
        if(not on_path[nxtR][nxtC]):
            res += solve(org_path, nxtR, nxtC, pos+1)
    on_path[row][col] = False
    return res

if __name__=="__main__":
    org_path = str(input())
    for i in range(9):
        on_path[0][i] = True
        on_path[8][i] = True
        on_path[i][0] = True
        on_path[i][8] = True

    ans = solve(org_path, 1, 1, 0)
    print(ans)
    exit(0)