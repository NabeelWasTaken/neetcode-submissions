class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        window = set(nums)
        output = 0
        for i in range(len(nums)):
            max_len = 0
            if (nums[i] - 1) not in window:
                max_len = 1
                num = nums[i]
                while (num + 1) in window:
                    max_len += 1
                    num+=1
            
            output = max(output, max_len)
        
        return output
                  
