from queue import SimpleQueue
from typing import NamedTuple, Mapping

class Node(NamedTuple):
    value: int
    neighbors: List['Node']
        
class Graph(NamedTuple):
    nodes: Mapping[int, Node]
        
class Solution:
    # god, this got ugly. I think early returns might be appropriate here.
    # not sure what I missed, pretty hungry & at the end of the day.
    # should get this pretty easily when I return to it.

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        elif n == 1:
            return True
        
        graph = Graph({})
        
        for n1, n2 in edges:
            for n in [n1, n2]:
                if n not in graph.nodes:
                    graph.nodes[n] = Node(n, [])
            
            node1 = graph.nodes[n1]
            node2 = graph.nodes[n2]
            
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
        
        # perform BFS on the node
        # current node must have one seen node at most,
        # and two children at most.
        seen = set()        
        queue = SimpleQueue()
        root = next(iter(
            node 
            for node in graph.nodes.values() 
            if len(node.neighbors) == 1
        ), None)
        
        if root:
            queue.put(root)
        
        res = root != None
        while queue.qsize() and res:
            curr = queue.get()
            res &= curr.value not in seen
            seen.add(curr.value)
            
            unseen_neighbors = [
                neighbor
                for neighbor in curr.neighbors
                if neighbor.value not in seen
            ]
            seen_neighbors = [
                neighbor
                for neighbor in curr.neighbors
                if neighbor.value in seen
            ]
            res &= len(unseen_neighbors) <= 2
            res &= len(seen_neighbors) <= 1
            
            for neighbor in unseen_neighbors:
                queue.put(neighbor)
        

        res &= len(seen) == len(graph.nodes)
        
        return res
