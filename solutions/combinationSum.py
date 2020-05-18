import copy

class Solution:    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        self.backtrack(solutions, target, [], candidates)
        return solutions
        
    def backtrack(self, solutions, target, temp_soln, candidates):
        if target == 0:
            solutions.append(copy.copy(temp_soln))
        elif target < 0:
            pass
        else:
            for i in range(len(candidates)):
                temp_soln.append(candidates[i])
                self.backtrack(solutions, target - candidates[i], temp_soln, candidates[i:])
                temp_soln.pop()
                
# also did this iteratively with a stack

