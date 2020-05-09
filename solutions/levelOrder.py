from queue import SimpleQueue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = SimpleQueue()
        queue.put(root)
        
        res = []
        
        level_count = 1
        curr_level = []
        
        while queue.qsize():
            curr = queue.get()
            level_count -= 1
            
            curr_level.append(curr.val)
                
            if curr.left:
                queue.put(curr.left)
            if curr.right:
                queue.put(curr.right)
            
            if not level_count:
                res.append(curr_level)
                level_count = queue.qsize()
                curr_level = []
        
        return res

