class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        

        
        # n = len(height)

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
            
            
            
        return res



        # for i in range(n):
        #     leftMax = rightMax = height[i]

        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
            
        #     for j in range(i + 1, n):
        #         rightMax = max(rightMax, height[j])
            

        #     res += min(leftMax, rightMax) - height[i]

        
        # return res