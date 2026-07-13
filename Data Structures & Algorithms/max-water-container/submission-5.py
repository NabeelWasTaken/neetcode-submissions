class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # [1, 7, 5, 6] = 12
        # [1, 2, 2, 2] = 4
        

        n = len(heights)

        l = 0
        maxArea = 0
        r = n - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return maxArea
            
            

            



       