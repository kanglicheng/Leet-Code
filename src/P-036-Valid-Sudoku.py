'''
P-036 - Valid Sudoku

Determine if a Sudoku is valid, according to:Sudoku Puzzles - The
Rules. The Sudoku board could be partially filled, where empty cells
are filled with the character'.'. A partially filled sudoku which is
valid. Note:A valid Sudoku board (partially filled) is not necessarily
solvable. Only the filled cells need to be validated.

Tags: Hash Table
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        # check row
        for data in board:
            if not self.isDuplicate(data):
                return False
        # check column
        for i in range(9):
            data = [board[k][i] for k in range(9)]
            if not self.isDuplicate(data):
                return False

        # check box
        for i in range(3):
            for j in range(3):
                data = [board[j * 3 + y][i * 3 + x] for y in range(3) for x in range(3)]
                if not self.isDuplicate(data):
                    return False

        return True

    def isDuplicate(self, l):
        s = filter(lambda x: x != '.', l)
        return len(set(s)) == len(s)

s = Solution()
l = [".........",
     "......3..",
     "...18....",
     "...7.....",
     "....1.97.",
     ".........",
     "...36.1..",
     ".........",
     ".......2."
     ]

print s.isValidSudoku(l)