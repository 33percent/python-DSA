class Queue:
    # queue implementation in python

    def __init__(self, *elements):
        self.data = []
        for element in elements:
            self.data.append(element)

    def enqueue(self, element):
        # add element to queue (overflow condition)
        self.data.append(element)

    def dequeue(self):
        # remove the first element in queue (underflow condition)
        self.data.pop(0)

    @property
    def front(self):
        # return the first element in queue
        return self.data[0]

    @property
    def rear(self):
        # return the last element in queue
        return self.data[len(self.data) - 1]

    def __repr__(self):
        return "Queue({})".format(self.data)

my_q = Queue(1,2,3,4)
print(my_q)

my_q.enqueue(5)
print(my_q)

my_q.dequeue()
print(my_q)

print(my_q.front)
print(my_q.rear)