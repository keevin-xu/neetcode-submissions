class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax = 0, 0
        for c in s:
            if c == "(":
                openMin, openMax = openMin + 1, openMax + 1
            elif c == ")":
                openMin, openMax = openMin - 1, openMax - 1
            else:
                openMin, openMax = openMin - 1, openMax + 1
            if openMax < 0:
                return False
            #  Because a wildcard can simply choose to be an empty string instead of a ), we floor openMin at 0.
            openMin = max(0,openMin)
        return openMin == 0

