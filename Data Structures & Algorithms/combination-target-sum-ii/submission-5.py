class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def backtrack(i, total, cur):

            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            backtrack(i + 1, total + candidates[i], cur)
            cur.pop()

            while i + 1 < len(candidates) and candidates[i+ 1] == candidates[i]:
                i += 1
            
            backtrack(i + 1, total, cur)
        
        backtrack(0, 0, [])
        return res