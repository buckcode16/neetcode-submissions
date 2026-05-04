class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            seen = set()

            for c in r:
                if c == '.':
                    continue
                if c in seen:
                    return False
                seen.add(c)

        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        for s in range(len(board)):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (s//3)*3+i
                    col = (s%3)*3+j
                    
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True