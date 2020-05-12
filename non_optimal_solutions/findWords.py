from collections import defaultdict
from typing import NamedTuple

class PathTuple(NamedTuple):
    path_entries: set
    first_coords: tuple
    last_coords: tuple
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        
        word_paths = defaultdict(list)
        for i in range(26):
            word_paths[chr(ord('a') + i)]
            
        for row, l in enumerate(board):
            for col, c in enumerate(l):
                coords = (row, col)
                path_tuple = PathTuple(set([coords]), coords, coords)
                word_paths[c].append(path_tuple)
        
        res = []
        for word in words:
            path_list = self.divide_and_conquer(word, word_paths, board)
            if path_list:
                res.append(word)
                
        return res
                
            
    def divide_and_conquer(self, word, word_paths, board):
        if word in word_paths:
            return word_paths[word]
        midpoint = len(word)//2
        first_half = word[0:midpoint]
        second_half = word[midpoint:len(word)]
        
        first_half_paths = self.divide_and_conquer(first_half, word_paths, board)
        second_half_paths = self.divide_and_conquer(second_half, word_paths, board)
        
        first_half_opts = defaultdict(list)
        
        for path_tup in first_half_paths:
            coords = path_tup.last_coords
            row, col = coords
            opts = [
                (row-1, col),
                (row+1, col),
                (row, col-1),
                (row, col+1)
            ]
            for r, c in opts:
                valid_move = (r >= 0 and r < len(board))\
                    and (c >=0 and c < len(board[0]))\
                    and (r,c) not in path_tup.path_entries
                
                if valid_move:
                    first_half_opts[(r,c)].append(path_tup)
        
        paths = []
        for second_path in second_half_paths:
            coords = second_path.first_coords
            row, col = coords
            if coords in first_half_opts:
                first_half_tups = first_half_opts[coords]
                for tup in first_half_tups:
                    if not tup.path_entries.intersection(second_path.path_entries):
                        new_tup = PathTuple(
                            tup.path_entries.union(second_path.path_entries),
                            tup.first_coords,
                            second_path.last_coords
                        )
                        paths.append(new_tup)
        word_paths[word] = paths
        return paths
