class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        stack = []
        res = []

        def backtrack(openCtr, closedCtr):

            if openCtr == closedCtr == n:
                res.append("".join(stack))
                return

            if openCtr < n:
                stack.append("(")
                backtrack(openCtr + 1, closedCtr)
                stack.pop()

            if closedCtr < openCtr:
                stack.append(")")
                backtrack(openCtr, closedCtr + 1)
                stack.pop()
            
        backtrack(0, 0)
        return res