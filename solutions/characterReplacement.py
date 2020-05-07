from collections import defaultdict

class Solution:
    # inefficient solution, but still scales at O(n).
    
    # it is inefficient, because the current character at the window
    # end will either be the largest character count, in which case
    # the window will expand, or the window would shrink because it will not,
    # maintain the invariant,
    # in which case, we need not consider it, as it will be smaller
    # than the previously stored maximum.

    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        character_counts = defaultdict(lambda: 0)
        
        window_start = 0
        max_window_size = 0
        
        for i in range(len(s)):
            curr = s[i]
            character_counts[curr] += 1
                
            while self.get_replacement_count(character_counts) > k:
                prev_char = s[window_start]
                window_start += 1
                character_counts[prev_char] -= 1                    
            
            max_window_size = max(max_window_size, i-window_start+1)
            
        return max_window_size
    
    def get_max_entry(self, d):
        max_char, max_val = None, -float('inf')
        for key, val in d.items():
            if val > max_val:
                max_char = key
                max_val = val
        
        return (max_char, max_val)
    
    def get_replacement_count(self, character_counts):
        replacement_count = 0
        max_character, _ = self.get_max_entry(character_counts)
        for char, count in character_counts.items():
            if char != max_character:
                replacement_count += count
            
        return replacement_count
            
