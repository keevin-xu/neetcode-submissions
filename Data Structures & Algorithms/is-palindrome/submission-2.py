class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [(n.lower() if n.isalpha() else n) for n in s if n.isalnum()]
        for i in range(len(chars) // 2):
            if chars[i] != chars[len(chars) - 1 - i]:
                return False
        return True