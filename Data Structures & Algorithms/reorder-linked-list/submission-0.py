# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast != None:
            if fast.next == None or fast.next.next == None:
                break
            else:
                fast = fast.next.next
                slow = slow.next
        if fast.next != None:
            fast = fast.next
        #reverse second half.
        p = slow
        c = slow.next
        n = c
        p.next = None
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n

        #merging
        c = head
        n = head
        n2 = p
        c2 = p
        while n.next != n2 and n2.next != n and n != n2:
            n = c.next
            n2 = c2.next
            c.next = c2
            c2.next = n
            c = n
            c2 = n2
        if n2 == n:
            return None
        elif n2.next == n:
            n.next = n2
            n2.next = None
        return None