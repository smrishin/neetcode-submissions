# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f = s = head
        # s will be at mid after this loop
        while f and f.next:
            s = s.next
            f = f.next.next
        
        # rotate the second half

        curr = s.next
        s.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        end = prev
        start = head

        while end:
            temp1 = start.next
            temp2 = end.next

            start.next = end
            end.next = temp1

            start = temp1
            end = temp2

