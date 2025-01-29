placed_column = set()
right_diagonal = set()
left_diagonal = set()
def solve(board, row):
    if row == 8:
        return 1
    ans = 0
    for col in range(8):
        if (board[row][col] == '.') and (col not in placed_column) and ((row+col) not in right_diagonal) and ((row-col) not in left_diagonal):
            placed_column.add(col)
            right_diagonal.add(row+col)
            left_diagonal.add(row-col)
            ans += solve(board, row+1)
            placed_column.remove(col)
            right_diagonal.remove(row+col)
            left_diagonal.remove(row-col)
    
    return ans

if __name__=="__main__":
    chess_board = []
    for i in range(8):
        chess_board.append(input())
    
    num_ways = solve(chess_board, 0)
    print(num_ways)
    exit(0)
