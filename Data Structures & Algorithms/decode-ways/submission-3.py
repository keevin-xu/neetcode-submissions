class Solution:
    def numDecodings(self, s: str) -> int:
        arr = [0] * (len(s) + 1)

        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        arr[1], arr[0] = 1, 1
        for i in range(2, len(s) + 1):
            # accessing s values, offset i by -1
            print(int(s[i-1-1:i]))
            if int(s[i-1-1:i+1-1]) == 0:
                return 0
            elif s[i-1] == '0' and int(s[i-1-1:i+1-1]) <= 26 and int(s[i-1-1:i+1-1]):
                arr[i] = arr[i-2]
            elif int(s[i-1-1:i+1-1]) <= 26 and int(s[i-1-1:i+1-1]) > 0 and not s[i-1 -1] == '0':
                arr[i] = arr[i-2] + arr[i-1]
            elif not s[i-1] == '0':
                arr[i] = arr[i-1]
            else:
                arr[i] = 0
        print(arr)
        return arr[len(s)]

# 12211
# [1, 2, 3, 5, 8]


