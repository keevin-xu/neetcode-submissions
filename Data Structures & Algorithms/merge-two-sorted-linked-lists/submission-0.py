# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        x = list1
        y = list2
        p = ListNode(0, None)
        while (x != None or y != None):
            if (x == None):
                p.next = y
                p = y
                y = y.next
            elif (y == None):
                p.next = x
                p = x
                x = x.next
            elif (x.val < y.val):
                p.next = x
                p = x
                x = x.next
            else:
                p.next = y
                p = y
                y = y.next
        if list1.val < list2.val:
            return list1
        return list2