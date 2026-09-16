class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 #if 0 mark the cell at the top of colum as 0
                    if r > 0:
                        matrix[r][0] = 0 #mark the left most cell of the row as 0 too
                    else:
                        rowZero = True #top row is 0s
        
        #change to 0s
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        #0, 0 used to mark if left column is 0s
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        #variable used to mark if top row is 0s
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0

        #since top row and left column used to mark if rows and columns are 0s, need 0,0 and variable to mark those two themeselves
        