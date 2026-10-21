class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        h = height
        lmax = h[l]
        rmax = h[r]

        out = 0
        # only move the side that has the lesser max
        while(l < r):
            if lmax < rmax:
                l += 1
                out += max(0, lmax - h[l])
                lmax = max(lmax, h[l])
            else:
                r -= 1
                out += max(0, rmax - h[r])
                rmax = max(rmax, h[r])
        return out

            