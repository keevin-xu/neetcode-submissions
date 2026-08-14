class Solution:
    def isValid(self, s: str) -> bool:
        pee = []
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                pee.append(s[i])
            else:
                if not pee:
                    return False
                x = pee.pop()
                if (x == '{' and s[i] == '}') or (x == '(' and s[i] == ')') or (x == '[' and s[i] == ']'):
                    continue
                else:
                    return False
        if pee:
            return False
        return True