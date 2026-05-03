class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}

        for i in range(len(nums)):
            
            res[nums[i]] = res.get(nums[i], 0) + 1
        

        pairs = [(count, nums) for nums, count in res.items()]
        
        pairs.sort()
    
        result = []
        for count, num in pairs[-k:]:
            result.append(num)
        
        return result




        
