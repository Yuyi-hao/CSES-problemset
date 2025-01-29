moves = []
def solve(n, fr, to, aux):
    if n == 0:
        return 0
    if n == 1:
        moves.append((fr, to))
        return 1
    count = 0
    count += solve(n-1, fr, aux, to)
    count += 1
    moves.append((fr, to))
    count += solve(n-1, aux, to, fr)
    return count
    
if __name__=="__main__":
    n = int(input())
    moves_cnt = solve(n, 1, 3, 2)
    print(moves_cnt)
    for x, y in moves:
        print(x, y)
    exit(0)
