# LIFO = last in first out
# adding and removing operation .
# adding = PUSH
# removing = POP

class Stack:
    def __init__(self):
        self.stack = []
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

#Use peek to look at the top of the stack

    def peek(self):
        return self.stack[-1]

#     removing an element
    def remove(self):
        if len(self.stack)<=0:
            return ("no element in the stack")
        else:
            return self.stack.pop()
aStack = Stack()
rStack = Stack()
aStack.add("Mon")
aStack.add("Tue")

aStack.peek()
print(aStack.peek())
print(aStack.peek())
aStack.add("thu")
print(aStack.peek())
rStack.add("january")
rStack.add("february")
rStack.add("march")
rStack.add("April")
print(rStack.remove())
print(rStack.remove())