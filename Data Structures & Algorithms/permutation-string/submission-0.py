class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1Count = {}
        s2Count = {}
        l = 0

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        for r in range(len(s2)):

            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1

            while (r - l + 1) > len(s1):
                s2Count[s2[l]] -= 1
                if s2Count.get(s2[l]) == 0:
                    del s2Count[s2[l]]
                l += 1
            
            if s1Count == s2Count:
                return True
            
        
        return False

        





