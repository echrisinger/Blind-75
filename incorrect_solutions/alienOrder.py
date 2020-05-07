from typing import Mapping, NamedTuple, Set
from queue import SimpleQueue

class Edge(NamedTuple):    
    parent: 'Node'
    child: 'Node'
    
    def __eq__(self, other):
        return self.parent.value == other.parent.value \
            and self.child.value == other.child.value
    
    def __hash__(self):
        tup = (self.parent.value, self.child.value)
        return hash(str(tup))
    
        
class Node(NamedTuple):
    value: str
    inbound_edges: Set[Edge]
    outbound_edges: Set[Edge]
    
class Graph(NamedTuple):
    nodes: Mapping[str, Node]
    edges: Mapping[tuple, Edge]
        
class Solution:
    # Incorrect because of a problem understanding, but solution of topological sort was correct.
    # Learning: Spend more time thinking about what the problem is saying beforehand.

    def alienOrder(self, words: List[str]) -> str:
        # perform a topological sort on the input letters
        graph = Graph({}, {})
        print(words)
        for word in words:
            for i, c in enumerate(word):
                if c not in graph.nodes:
                    node = Node(c, set(), set())
                    graph.nodes[c] = node
                else:
                    node = graph.nodes[c]
                
                if i != 0 and word[i-1] != word[i]:
                    parent_char = word[i-1]
                    parent_node = graph.nodes[parent_char]
                    edge_tuple = (parent_char, word[i])
                    
                    if edge_tuple not in graph.edges:
                        edge = Edge(parent_node, node)
                        graph.edges[edge_tuple] = edge
                    else:
                        edge = graph.edges[edge_tuple]

                    if edge not in parent_node.outbound_edges:
                        parent_node.outbound_edges.add(edge)
                        
                    if edge not in node.inbound_edges:                    
                        node.inbound_edges.add(edge)
                    
        sources = SimpleQueue()
        for node in graph.nodes.values():
            if not len(node.inbound_edges):
                sources.put(node)
        
        sorting = []
        while sources.qsize():
            next_sources = SimpleQueue()
            while sources.qsize():
                curr = sources.get()
                child_nodes = [edge.child for edge in curr.outbound_edges]
                for child in child_nodes:
                    edge_tuple = (curr.value, child.value)
                    # keep graph & nodes in sync
                    edge = graph.edges[edge_tuple]
                    del graph.edges[edge_tuple]
                    child.inbound_edges.remove(edge)
                    if not len(child.inbound_edges):
                        next_sources.put(child)
                    
                del graph.nodes[curr.value]
                sorting.append(curr.value)
            
            sources = next_sources
            
        return "".join(sorting) \
            if not len(graph.nodes) \
            else ""

