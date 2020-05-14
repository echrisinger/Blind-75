# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # doesn't work, but that's because the input is totally unclear
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_nodes = {}
        stk = [node]
            
        while stk:
            curr = stk.pop()
            if curr.val in new_nodes:
                continue
                
            new_node = Node(curr.val)
            new_nodes[curr.val] = new_node            
            
            for ne in curr.neighbors:
                if ne.val in new_nodes:
                    new_node.neighbors.append(ne)
                    ne.neighbors.append(new_node)
                else:
                    stk.append(ne)
        return new_nodes[node.val]
