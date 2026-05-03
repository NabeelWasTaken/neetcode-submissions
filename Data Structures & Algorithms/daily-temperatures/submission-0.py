class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            
            while stack and n > stack[-1][1]:
                stackInd, StackT = stack.pop()
                res[stackInd] = (i - stackInd)

            stack.append([i , n])
        
        return res
