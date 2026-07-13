class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        zero_cnt = 0
        value = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
            
            else:
                value *= nums[i]
            
        
        for i in range(len(nums)):

            if zero_cnt > 1:      
                output.append(0)
            elif zero_cnt == 1:
                if nums[i] == 0:
                    output.append(value)
                else:
                    output.append(0)
            
            else:
                output.append(value// nums[i])

            
        return output
            



            
