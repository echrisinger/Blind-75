class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indicator = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                indicator = min(matrix[i][j], indicator)
        indicator -= 1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    for r in range(len(matrix)):
                        # if not a 0 set to indicator
                        if matrix[r][j]: 
                            matrix[r][j] = indicator
                    for c in range(len(matrix[0])):
                        if matrix[i][c]:
                            matrix[i][c] = indicator
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == indicator:
                    matrix[i][j] = 0
        
# O(mn) time, O(1) space
