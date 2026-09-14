class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) in rows[i] or int(board[i][j]) in cols[j] or int(board[i][j]) in squares[((i//3),(j//3))]:
                    return False
                rows[i].add(int(board[i][j]))
                cols[j].add(int(board[i][j]))
                squares[((i//3),(j//3))].add(int(board[i][j]))
        return True
                