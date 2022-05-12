# Runtime: 108 ms, faster than 69.70% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.8 MB, less than 99.12% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            hashtable = {}
            hashset = {}
            for j in range(9):
                if board[i][j] != '.':
                    #checking row
                    if board[i][j] in hashtable:
                        return False
                    else:
                        hashtable[board[i][j]] = 1
                #checking column
                if board[j][i]!='.':
                    if board[j][i] in hashset:
                        return False
                    else:
                        hashset[board[j][i]] = 1
                if i%3==0 and j%3==0:
                    square = {}
                    for k in range(3):
                        for l in range(3):
                            if board[i+k][j+l]!='.':
                                if board[i+k][j+l] in square:
                                    return False
                                else:
                                    square[board[i+k][j+l]] = 1
        return True