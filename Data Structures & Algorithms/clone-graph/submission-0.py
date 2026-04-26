"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        adj = {}
        q = deque()
        q.append(node)
        visit = set()
        visit.add(node)
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.val not in adj:
                        adj[curr.val] = Node(val = curr.val)
                for n in curr.neighbors:
                    if n.val not in adj:
                        adj[n.val] = Node(val = n.val)
                    adj[curr.val].neighbors.append(adj[n.val])
                    if n not in visit:
                        q.append(n)
                        visit.add(n)
        return adj[1]
        