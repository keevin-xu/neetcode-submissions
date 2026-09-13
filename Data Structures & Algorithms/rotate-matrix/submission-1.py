class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp = 0
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix) // 2):
            for j in range(len(matrix)):
                temp = matrix[j][i]
                matrix[j][i] = matrix[j][len(matrix) - 1 - i]
                matrix[j][len(matrix) - 1 - i] = temp