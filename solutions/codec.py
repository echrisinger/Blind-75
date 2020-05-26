# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        stk = [root]

        while stk:
            curr = stk.pop()
            if not curr:
                res.append('#')
                continue
            res.append(str(curr.val))
            stk.append(curr.right)
            stk.append(curr.left)
                        
        return ','.join(res)        
        
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
            
        :type data: str
        :rtype: TreeNode
        """
        a = data.split(',')
        if not a:
            return None
        
        it = iter(a)
        def doit():
            curr = next(it)
            if curr == '#':
                return None
            
            node = TreeNode(int(curr))
            node.left = doit()
            node.right = doit()
            
            return node
        
        return doit()        
            
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# O(n) time, space.
# Not super pretty.
# could be made iterative by using a stack and adding to an index.
