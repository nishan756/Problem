from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                box_index = (i // 3) * 3 + (j // 3)
                
                if val in rows[i] or val in cols[j] or val in sub_box[box_index]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                sub_box[box_index].add(val)
        return True
        
