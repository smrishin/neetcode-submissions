# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque([root])

        while q:
            curr = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                curr.append(node.val)
                q.append(node.left)
                q.append(node.right)

            res.append(curr[:]) if curr else None
        return res