# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        inorder_indices = {}
        for i, val in enumerate(inorder):
            inorder_indices[val] = i
        
        return self.helper(preorder, inorder, 0, len(preorder),  0, len(inorder), inorder_indices)

    def helper(self, preorder, inorder, pre_s, pre_e, in_s, in_e, inorder_indices):
        if pre_s == pre_e or pre_s >= len(preorder) or pre_s < 0:
            return None
        
        curr = preorder[pre_s]
        inorder_idx = inorder_indices[curr]
        left_len = (inorder_idx - in_s)
        l_pre_s = pre_s + 1
        l_pre_e = l_pre_s + left_len
        
        left_node = self.helper(
            preorder,
            inorder,
            l_pre_s,
            l_pre_e,
            in_s,
            inorder_idx,
            inorder_indices
        )
        right_node = self.helper(
            preorder,
            inorder,
            l_pre_e,
            pre_e,
            inorder_idx + 1,
            in_e,
            inorder_indices
        )
        
        return TreeNode(curr, left_node, right_node)

# O(n) time, space.

