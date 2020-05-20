# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import SimpleQueue

class Codec:
    # correct method is to do a preorder traversal
    # so you don't need to store excess nil values
    # this approach poses a problem when the tree is sparse.

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        level = SimpleQueue()
        level.put(root)
        level_count = 1 if root else 0
        
        res = []
        while level_count:
            next_level_count = 0
            next_level = SimpleQueue()
            while level.qsize():
                curr = level.get()  
                if curr:
                    val = str(curr.val)
                    for node in [curr.left, curr.right]:
                        next_level.put(node)
                        if node:
                            next_level_count += 1
                else:
                    val = ''
                    next_level.put(None)
                    next_level.put(None)
                
                res.append(val)
                
            level_count = next_level_count
            level = next_level
        
        
        return ','.join(res)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
            
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        arr = data.split(',')
        stk = [0]
        nodes = {}
        treenode_factory = lambda val: TreeNode(int(val)) if val != '' else None
        while stk:
            curr_idx = stk.pop()
            curr_node = treenode_factory(arr[curr_idx])
            nodes[curr_idx] = curr_node
            
            if curr_idx != 0: # attach curr node to parent
                parent_idx = (curr_idx-1) // 2
                if nodes[parent_idx]: # account for nil parent
                    if curr_idx % 2: # left
                        nodes[parent_idx].left = curr_node
                    else:
                        nodes[parent_idx].right = curr_node
                

            if (curr_idx * 2 + 1) < len(arr) and curr_node:
                stk.append(curr_idx * 2 + 2)
                stk.append(curr_idx * 2 + 1)
        
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
