from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        
        for w in strs:
            key = self.hash(w)
            words[key].append(w)
            
        return list(words.values())
    
    def hash(self, s):
        counts = Counter(s)
        tup = []
        for i in range(26):
            letter = chr(ord('a')+i)
            count = 0
            if letter in counts:
                count = counts[letter]
            tup.append(count)
        
        return tuple(tup)

