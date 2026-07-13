class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        mapper = defaultdict(list)

        for s in strs:
            str_group = [0] * 26
            for c in s:
                pos = ord('z') - ord(c)
                str_group[pos] += 1
            mapper[tuple(str_group)].append(s)
        return list(mapper.values())
        
        
        