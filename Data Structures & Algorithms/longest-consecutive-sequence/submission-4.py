class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        numsSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numsSet:

                current_num = num
                length = 1

                while current_num + 1 in numsSet:
                    current_num += 1
                    length += 1

                longest = max(length, longest)

        return longest
            
