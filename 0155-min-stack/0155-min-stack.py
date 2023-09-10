class MinStack(object):

    def __init__(self):
        self.head = -1
        self.arr = []
        self.minStack = []
        self.min = 1000000000000

    def push(self, val):
        self.head +=1 
        self.arr.append(val)
        if (val < self.min):
            self.min = val
        self.minStack.append(self.min)
        
         
        

    def pop(self):
        self.head -=1
        self.arr.pop()
        self.minStack.pop()
        if len(self.minStack) == 0:
            self.min = 1000000000000
        else:
            self.min = self.minStack[-1]


    def top(self):
        return self.arr[self.head]
        

    def getMin(self):
        return self.minStack[self.head]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()