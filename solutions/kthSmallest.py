# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stk = []
        while root:
            stk.append(root)
            root = root.left
                    
        while stk and k:
            curr = stk.pop()
            k -= 1
            if curr.right:
                right = curr.right
                while right:
                    stk.append(right)
                    right = right.left
                
        return curr.val
    

