class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, value in enumerate(nums):

            if value > 0:
                break
            
            if i > 0 and value == nums[i - 1]:
                continue

            
            
            l = i+1
            r = len(nums) - 1

            while l < r:
                totSum = value + nums[l] + nums[r]

                if totSum < 0:
                    l += 1
                elif totSum > 0:
                    r -= 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                

        
        return res