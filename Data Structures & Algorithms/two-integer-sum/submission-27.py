class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        exists = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in exists:
                return [ exists.get(diff, 0), i]
            
            exists[nums[i]] = i
        
        return -1
            
                
    


            
        
                    

        