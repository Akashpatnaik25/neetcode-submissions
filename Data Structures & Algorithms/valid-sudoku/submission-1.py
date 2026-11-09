class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        board_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                board_index = r//3 *3 + c//3
                num = board[r][c]
                if (num in row[r]) or (num in col[c]) or (num in board_set[board_index]):
                    return False
                
                row[r].add(num)
                col[c].add(num)
                board_set[board_index].add(num)
        return True 