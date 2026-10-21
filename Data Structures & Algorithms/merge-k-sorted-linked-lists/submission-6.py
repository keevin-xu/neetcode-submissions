# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        out = []
        counter = 0

        # need a way to break ties between priority values.
        # so use counter to guarantee unique id for each
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        
        # dummy
        head = ListNode()
        curr = head
        while heap:
            newnode = heapq.heappop(heap)

            if newnode[2].next:
                counter += 1
                heapq.heappush(heap, (newnode[2].next.val, counter, newnode[2].next))

            curr.next = newnode[2]
            curr = curr.next
        
        return head.next