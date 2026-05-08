# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS iterative
        s = []
        curr = root
        count = 0

        while True:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right


        # DFS Recursive
        # res = []

        # def inorder(node):
        #     if not node:
        #         return
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return res[k-1]