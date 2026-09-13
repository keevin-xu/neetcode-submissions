class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        v = len(matrix)
        h = len(matrix[0])
        loop = (min(len(matrix), len(matrix[0]))+1) // 2
        for i in range(loop):
            if v <= 1 and h <= 1:
                out.append(matrix[i][i])
                break
            elif v <= 1:
                for j in range(h):
                    out.append(matrix[i][i+j])
                break
            elif h <= 1:
                for j in range(v):
                    out.append(matrix[i+j][i])  
                break
            else:      
                for j in range(h):
                    out.append(matrix[i][i+j])
                for k in range(v-1):
                    out.append(matrix[i+k+1][len(matrix[0])-1-i])
                for j in range(h-1):
                    out.append(matrix[len(matrix)-1-i][len(matrix[0])-1-1-i-j])
                for k in range(v-2):
                    out.append(matrix[len(matrix)-1-1-i-k][i])
            v -= 2
            h -= 2 
        return out