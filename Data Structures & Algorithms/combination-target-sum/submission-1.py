class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, total,subset):
            
            
            if target == total:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            
            subset.append(nums[i])
            backtrack(i, total + nums[i], subset)

            subset.pop()
            backtrack(i + 1, total, subset)
        
        backtrack(0, 0, [])
        return res
        

