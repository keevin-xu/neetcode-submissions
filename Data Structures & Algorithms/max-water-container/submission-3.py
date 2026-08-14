class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = 0
        k = 1
        max = 0
        best = min(heights[i], heights[k]) * (k - i)
        while (k < len(heights)):            
            if min(heights[i], heights[k]) * (k - i) > best:
                best = min(heights[i], heights[k]) * (k - i)
            if min(heights[j], heights[k]) * (k - j) > best:
                best = min(heights[j], heights[k]) * (k - j)
                i = j
            elif min(heights[i+1], heights[k]) * (k - i - 1) > best:
                i+=1
                continue
            if (heights[k] > heights[j]):
                j = k
            k += 1
        return best