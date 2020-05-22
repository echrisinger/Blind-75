# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class DPNode:
    def __init__(self, subpath, total_path):
        self.subpath = subpath
        self.max = total_path
        
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.getDPTree(root).max
        
    def getDPTree(self, root: TreeNode) -> DPNode:
        if not root:
            return DPNode(-float('inf'), -float('inf'))
        
        left = self.getDPTree(root.left)
        right = self.getDPTree(root.right)
        
        max_subpath = root.val + max(0, left.subpath, right.subpath)
        max_path = max(
            max_subpath,
            root.val + left.subpath + right.subpath,
            left.max,
            right.max
        )
        res = DPNode(max_subpath, max_path)
        return res
# O(n) time, O(n) space if unbalanced else O(log(n))
