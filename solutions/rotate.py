class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s = matrix
        for row in range(len(matrix) // 2):
            for col in range(len(matrix) // 2):
                r1 = matrix[row][col]
                r2 = matrix[col][len(s)-1-row]
                l2 = matrix[len(s)-1-row][len(s)-1-col]
                l1 = matrix[len(s)-1-col][row]
                
                matrix[row][col] = l1
                matrix[col][len(s)-1-row] = r1
                matrix[len(s)-1-row][len(s)-1-col] = r2
                matrix[len(s)-1-col][row] = l2
                
        if len(matrix) % 2:
            mid = len(matrix) // 2
            for row in range(mid):
                right = matrix[row][mid]
                bottom = matrix[mid][len(s)-1-row]
                left = matrix[len(s)-1-row][mid]
                top = matrix[mid][row]
                
                matrix[row][mid] = top
                matrix[mid][len(s)-1-row] = right
                matrix[len(s)-1-row][mid] = bottom
                matrix[mid][row] = left
        
