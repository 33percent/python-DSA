class Stack:
    # stack implementation

    def __init__(self, *elements):
        self.data = []
        for element in elements:
            self.data.append(element)

    def push(self,element):
        #add an element to the stack
        self.data.append(element)

    def pop(self):
        # remove the top most element
        try:
            self.data.pop()
            return True
        except IndexError as e:
            return False

    def top(self):
        # get the top most element in stack
        pass

    def size(self):
        # return the size of the stack
        return len(self.data)

    def empty(self):
        # check if the stack is empty or not
        if self.size() > 0:
            return False
        return True

    def __repr__(self):
        return "Stack({})".format(self.data)


my_stack = Stack(1)
print(my_stack.size())
my_stack.push(2)
my_stack.push(3)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack)