class MinStack:

    def __init__(self):
        self.stack=[]
        self.minArray=[]
        
    def push(self, val: int) -> None:
        if(len(self.minArray)):
            if(val <= self.minArray[-1]):
                self.minArray.append(val)
        else:
            self.minArray.append(val)
        self.stack.append(val) 

    def pop(self) -> None:
        
        if (self.stack[-1]==self.minArray[-1]):
            self.minArray.pop()
        self.stack.pop()

    def top(self) -> int:
        return (self.stack[-1])

    def getMin(self) -> int:
        return (self.minArray[-1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
