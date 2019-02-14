class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
        return self.stack.append(val)
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        return self.size() == 0
        
        
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.insert(0,val)
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return self.size() == 0
        
        
block=Stack()
print (block.size())
block.push(1)
print (block.pop())
print (block.pop())