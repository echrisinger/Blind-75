# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not (p and q):
            return not (p or q)
        
        return p.val == q.val and self.isSameTree(p.left, q.left)\
            and self.isSameTree(p.right,q.right)

# O(n) time, O(n) space (unless balanced tree constraint)
