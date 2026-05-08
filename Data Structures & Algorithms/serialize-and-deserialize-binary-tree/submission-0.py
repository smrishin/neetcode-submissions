# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node is None:
                res.append('#')
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ','.join(res)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "#":
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q:
            curr = q.popleft()

            if vals[i] != "#":
                curr.left = TreeNode(int(vals[i]))
                q.append(curr.left)
            i += 1
            if vals[i] != "#":
                curr.right = TreeNode(int(vals[i]))
                q.append(curr.right)
            i += 1
        return root



        

