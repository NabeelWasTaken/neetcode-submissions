class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        # self.minStack.append(math.inf)
        

    def push(self, val: int) -> None:


        
        # self.minStack.append(val)
        self.stack.append(val)

        if self.minStack:
            current_min = min(val, self.minStack[-1])
            self.minStack.append(current_min)
        
        else:
            self.minStack.append(val)
        

        

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
