class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ctr = defaultdict(int)

        for n in nums:
            ctr[n] += 1
        
        # cnt_list = [] * (len(nums) + 1)
        cnt_list = [[] for i in range(len(nums) + 1)]
        for nums, i in ctr.items():
            cnt_list[i].append(nums)
        
        
        output = []
        for i in range(len(cnt_list) - 1, -1, -1):
            for num in cnt_list[i]:
                output.append(num)
            
            if len(output) == k:
                return output
            
        return -1



        
        
        
            