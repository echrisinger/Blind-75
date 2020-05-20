# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not (s and t):
            return not (s or t)
        elif self.isSame(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
                    
    def isSame(self, s, t):
        if not (s and t):
            return not (s or t)
        
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

# O(st)
