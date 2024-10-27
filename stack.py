class Stack:
    def __init__(self) -> None:
        self.array = []
        self.size = 0
        
    def push(self, x : int) -> None:
        self.array.append(x)
        self.size += 1
    
    def pop(self) -> None:
        if(self.size == 0):
            raise Exception("stack is empty")
        self.array.pop(self.size-1)
        self.size -= 1
    
    def top(self):
        if(self.size == 0):
            raise Exception("stack is empty")
        return self.array[self.size-1]
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        pass
    # You can implement this class however you like