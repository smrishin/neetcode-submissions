# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(preorder[0])
        inorderRootIndex = inorder.index(root.val)

        inL = inorder[:inorderRootIndex]
        inR = inorder[inorderRootIndex + 1:]

        preL = preorder[1 : len(inL) + 1]
        preR = preorder[len(inL) + 1 : ]

        root.left = self.buildTree(preL, inL)
        root.right = self.buildTree(preR, inR)

        return root







