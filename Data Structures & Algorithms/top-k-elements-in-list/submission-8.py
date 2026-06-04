class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
    

        output = []
        for i in range(len(freq) - 1,0, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
        return output
        
            