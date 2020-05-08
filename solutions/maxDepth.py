# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        ) + 1

    def maxDepthPreorder(self, root: TreeNode) -> int:
        stack = []
        level = 1
        
        while root != None:
            stack.append((root, level))
            root = root.left
            level += 1
        
        max_depth = 0
        while len(stack):
            node, level = stack.pop()
            max_depth = max(max_depth, level)

            child = node.right
            
            while child:
                level += 1
                max_depth = max(max_depth, level)
                stack.append((child, level))                
                child = child.left
                
        return max_depth
