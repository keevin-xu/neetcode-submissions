class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1

            # shift by 31 - i to get all the way to the left position first.
            result = result | (bit << (31 - i))
        return result