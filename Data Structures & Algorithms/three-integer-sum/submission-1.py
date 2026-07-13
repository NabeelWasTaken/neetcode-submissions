class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # [-1, 2, 1, 0, -1, 3, 1] = [[-1, 2, -1], [1, 0, -1]]

        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            first_element = nums[i]
            l = i + 1
            r = n - 1

            while l < r:
                curSum = first_element + nums[l] + nums[r]
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    output.append([first_element, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                
        
        return output

    
        




        


        