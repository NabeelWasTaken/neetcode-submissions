class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                a = stack.pop()
                stack.append(stack.pop() - a)
            elif c == "/":
                a = stack.pop()
                stack.append(int(stack.pop()/a))
            else:
                stack.append(int(c))
            
        return stack[0]


            