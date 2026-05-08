# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next

        prev = None
        curr = s.next
        s.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l1, l2 = head, prev

        D = node = ListNode()

        while l1 and l2:
            node.next = l1
            l1 = l1.next
            node = node.next
            
            node.next = l2
            l2 = l2.next
            node = node.next

        node.next = l1 or l2