from queue import SimpleQueue

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.inbound = set()
        self.outbound = set()
        
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [None]*26
        
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        try:
            nodes = self.getGraph(words)
        except ValueError:
            return ''
        sources = [
            node
            for node in nodes
            if node and not node.inbound
        ]
        q = SimpleQueue()
        for s in sources:
            q.put(s)
            
        res = []
        seen = set()
        
        while q.qsize():
            curr = q.get()
            if curr.val in seen:
                continue
            seen.add(curr.val)
            res.append(curr.val)
            
            for n in curr.outbound:
                node = nodes[self._to_idx(n)]
                node.inbound.remove(curr.val)
                
                if not node.inbound:
                    q.put(node)
                
        return ''.join(res) if len(seen) == len(list(filter(None, nodes))) else ''
            
    def getGraph(self, words) -> List[GraphNode]:
        root = TrieNode('')
        nodes = [None]*26
        
        for w in words:
            curr = root
            for c in w:
                idx = self._to_idx(c)
                if not nodes[idx]:
                    nodes[idx] = GraphNode(c)

                if not curr.children[idx]:
                    curr.children[idx] = TrieNode(c)
                    
                for child in curr.children:
                    if child and child.val != c:
                        nodes[idx].inbound.add(child.val)
                        nodes[self._to_idx(child.val)].outbound.add(c)


                curr = curr.children[idx]
                
            if any(curr.children):
                raise ValueError('Unexpected ordering')
                
        return nodes
                
                
    def _to_idx(self, c):
        return ord(c) - ord('a')
    
    def _to_chr(self, i):
        return chr(ord('a') + i)

