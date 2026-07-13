class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        first = [0] * 26
        second = [0] * 26

        for c in s:
            pos = ord('z') - ord(c)
            first[pos] += 1
        
        for c in t:
            pos = ord('z') - ord(c)
            second[pos] += 1

        
        return first==second
        
        

            
            
