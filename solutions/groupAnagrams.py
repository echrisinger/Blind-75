class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize map
        record = {}
        
        # hash each string to an integer
        for s in strs:
            # assign map key => str
            hash_repr = self._hashStr(s)
            if hash_repr not in record:
                record[hash_repr] = []
            
            record[hash_repr].append(s)
        
        # map comprehension => list
        return record.values()
        
        
    def _hashStr(self, s: str) -> int:
        char_counts = self._get_char_counts(s)
        total = 0
        running_count = 0
        for i,n in enumerate(char_counts):
            while n != 0:
                # compute addition to the total
                total += (i+1) * (27**running_count)
                # increment running_count
                running_count += 1
                # decrement count
                n -= 1
                
        return total
    
    def _get_char_counts(self, s: str) -> List[int]:
        """
        Returns: Fixed length (26) array of counts in lowercase alphabet character set
        """
        counts = [0 for _ in range(26)]
        
        for c in s:
            c_repr = ord(c) - ord('a')
            counts[c_repr] += 1
        
        return counts
