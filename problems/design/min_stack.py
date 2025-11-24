# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# -----------------------------

class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        curr_min = self.min_stack[-1] if self.min_stack else float("inf")
        self.min_stack.append(min(curr_min, val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else 0
    
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1
