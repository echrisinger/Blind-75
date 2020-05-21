# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRec(root, -float('inf'), float('inf'))
        
    def isValidBSTRec(self, root, f, c) -> bool:
        if not root:
            return True
        
        return f < root.val < c\
            and self.isValidBSTRec(root.left, f, root.val)\
            and self.isValidBSTRec(root.right, root.val, c)
        
# O(n) time, O(n) space unless balanced in which case O(log(n))
