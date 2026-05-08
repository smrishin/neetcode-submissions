# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeLists(self, l1, l2):
        D = node = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 or l2

        return D.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        D = node = ListNode(float("-inf"), None)

        for l in lists:
            node = self.mergeLists(node, l)
        
        return D.next
            
        
    