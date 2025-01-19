visited = [[False]*7 for _ in range(7)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

direc = {
    # row, col
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
def isValid(val):
    return val >= 0 and val < 7

def solve(org_path, row, col, pos):
    if pos == len(org_path):
        return 1 if (row==6 and col==0) else 0
    
    if (row==6 and col==0):
        return 0

    if visited[row][col]:
        return 0
    
    seen = [-1]*4
    for i in range(4):
        if isValid(row+dr[i]) and isValid(col+dc[i]):
            seen[i] = visited[row+dr[i]][col+dc[i]]
    
    if not seen[2] and not seen[3] and seen[0] and seen[1]:
        return 0
    
    if not seen[0] and not seen[1] and seen[2] and seen[3]:
        return 0
    
    if isValid(row-1) and isValid(col+1) and visited[row-1][col+1]:
        if not seen[0] and not seen[3]:
            return 0
        
    if isValid(row+1) and isValid(col+1) and visited[row+1][col+1]:
        if not seen[0] and not seen[2]:
            return 0
        
    if isValid(row-1) and isValid(col-1) and visited[row-1][col-1]:
        if not seen[1] and not seen[3]:
            return 0
    
    if isValid(row+1) and isValid(col-1) and visited[row+1][col-1]:
        if not seen[1] and not seen[2]:
            return 0
    
    
    visited[row][col] = True
    ans = 0
    if org_path[pos] != "?":
        dir = org_path[pos]
        if isValid(row+direc[dir][0]) and isValid(col+direc[dir][1]):
            ans += solve(org_path, row+direc[dir][0], col+direc[dir][1],  pos+1)
    else:
        for dir, dic in direc.values():
            if isValid(row+dir) and isValid(col+dic):
                ans += solve(org_path, row+dir, col+dic, pos+1)

    
    
    visited[row][col] = False
    return ans

if __name__=="__main__":
    org_path = str(input())
    ans = solve(org_path, 0, 0, 0)
    print(ans)
    exit(0)