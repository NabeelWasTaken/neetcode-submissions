class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        output = math.inf
        while l <= r:

            if nums[l] <= nums[r]:
                output = min(nums[l], output)
                break
            
            m = (l+r) // 2
            output = min(nums[m], output)
            if nums[m] >= nums[l]:
                l = m + 1
            
            else:
                r = m - 1

        return output
