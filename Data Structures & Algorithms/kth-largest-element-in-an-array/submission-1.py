import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            curr = heapq.heappop(heap)
            heapq.heappush(heap, max(nums[i], curr))
        return heapq.heappop(heap)