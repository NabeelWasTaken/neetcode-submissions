class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []
        parMap = {")" : "(" , "}" : "{", "]" : "["}

        for c in s:
            if stack and stack[-1] == parMap.get(c):
                stack.pop()
            
            else:
                stack.append(c)
            
        if len(stack) == 0:
            return True
        else:
            return False
