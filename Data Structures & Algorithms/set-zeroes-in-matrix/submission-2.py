class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #Using a single variable: To avoid this collision, you introduce a single standalone variable (such as a boolean flag like isFirstRowZero or isFirstColZero) to handle the state of the first row (or column) completely independently. This frees up matrix[0][0] to safely manage the other.
        isFirstColumn = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0 and matrix[i][j] == 0:
                    isFirstColumn = True
                    continue
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0 or i == 0:
                    continue
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        for i in range(len(matrix[0])):
            if matrix[0][0] == 0:
                matrix[0][i] = 0
        for i in range(len(matrix)):
            if isFirstColumn:
                matrix[i][0] = 0