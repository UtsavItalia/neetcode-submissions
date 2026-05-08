# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        stack = [[root, 1]]
        result = 0
        # self.maxDepth(root.right)
        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, 1 + depth])
                stack.append([node.right, 1 + depth])
        return result