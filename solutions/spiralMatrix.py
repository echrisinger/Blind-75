class Solution:
    # supplying an imperative & recursive solution.
    
    # needs to descend the middle:
    # 2 5 5
    # 8 4 2
    # 0 1 3
    # 1 1 1
    
    # needs to go right across the middle
    # 2 5 5 1
    # 8 4 2 1
    # 0 1 3 1
    
    # no action
    # 1 1 1
    # 1 1 1
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        spiral_count = 0
        row_count = len(matrix)
        col_count = len(matrix[0])
        side_lengths = [row_count, col_count]
        
        spiral = []
        while all([spiral_count < int(length / 2) for length in side_lengths]):
            for col in range(spiral_count, col_count-spiral_count-1):
                curr = matrix[spiral_count][col]
                spiral.append(curr)
                
            for row in range(spiral_count, row_count-spiral_count-1):
                far_col = len(matrix[0])-1-spiral_count
                curr = matrix[row][far_col]
                spiral.append(curr)
                
            for col in range(col_count-spiral_count-1, spiral_count, -1):
                far_row = len(matrix)-1-spiral_count
                curr = matrix[far_row][col]
                spiral.append(curr)
                
            for row in range(row_count-spiral_count-1, spiral_count, -1):
                curr = matrix[row][spiral_count]
                spiral.append(curr)
            
            spiral_count += 1
            
        # handle edge case of single row or column
        # could be handled more gracefully by checking if the back direction
        # is the same as the forward above.
        odd_col = col_count % 2
        odd_row = row_count % 2
        if spiral_count < int(row_count / 2) and odd_col:
            # descend the missing column
            for row in range(spiral_count, row_count-spiral_count):
                curr = matrix[row][spiral_count]
                spiral.append(curr)
        elif spiral_count < int(col_count / 2) and odd_row:
            # go right along middle
            for col in range(spiral_count, col_count-spiral_count):
                curr = matrix[spiral_count][col]
                spiral.append(curr)
        elif odd_col and odd_row and row_count == col_count:
            spiral.append(matrix[spiral_count][spiral_count])
        
        return spiral

    def spiralOrderRecursive(self, matrix: List[List[int]]) -> List[int]:
        
