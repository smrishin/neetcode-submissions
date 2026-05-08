"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[curr].neighbors.append(oldToNew[nei])
        return oldToNew[node]

        # # DFS
        # oldToNew = {}

        # def dfs(node):
        #     if not node:
        #         return None
        #     if node in oldToNew:
        #         return oldToNew[node]

        #     copy = Node(node.val)

        #     oldToNew[node] = copy

        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy
        # return dfs(node)
