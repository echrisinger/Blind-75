# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

RECURSIVE_SOLN = False

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        least, greatest = (p, q) if p.val < q.val else (q, p)
        if RECURSIVE_SOLN:
            return self.recursive_soln(root, least, greatest)
        return self.iterative_soln(root, least, greatest)
        
    def recursive_soln(self, root: 'TreeNode', l: 'TreeNode', g: 'TreeNode'):
        if root.val >= l.val and root.val <= g.val:
            return root
        
        new_root = root.left if root.val > g.val else root.right
        return self.recursive_soln(new_root, l, g)
            
    
    def iterative_soln(self, root: 'TreeNode', l: 'TreeNode', g: 'TreeNode'):
        while not (root.val >= l.val and root.val <= g.val):
            if root.val > l.val:
                root = root.left
            else:
                root = root.right
                
        return root
