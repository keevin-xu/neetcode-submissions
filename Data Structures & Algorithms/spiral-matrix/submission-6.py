class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1
        out=[]
        def help(l,r,t,b):
            for i in range(l,r+1):
                out.append(matrix[t][i])
            for i in range(t+1,b+1):
                out.append(matrix[i][r])
            for i in range(r-l):
                out.append(matrix[b][r-i-1])
            for i in range(b-t-1):
                out.append(matrix[b-i-1][l])
        while l < r and t < b:
            help(l,r,t,b)
            l += 1
            r -= 1
            t += 1
            b -= 1
        if t == b and l == r:
            out.append(matrix[l][t])
        elif t == b:
            for i in range(l,r+1):
                out.append(matrix[t][i])
        elif l == r:
            for i in range(t,b+1):
                out.append(matrix[i][l])
        return out