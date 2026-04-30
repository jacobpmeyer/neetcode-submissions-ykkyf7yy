# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        md = depth
        def dfs(node, depth, md):
            if root is None:
                return md
            depth += 1
            md = max(depth, md)
            if node.left:
                md = dfs(node.left, depth, md)
            if node.right:
                md = dfs(node.right, depth, md)
            depth -= 1
            return md
        return dfs(root, depth, md)