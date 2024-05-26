def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1
def enqueue(self, value):
        if ((self.rear + 1) % self.k == self.front):
            print("Circular Queue is Full\n")
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.k
def dequeue(self):
        if (self.front == self.rear):
            print("Circular Queue is Empty\n")
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return temp
def front(self):
        if (self.front == self.rear):
            print("No element in the Circular Queue\n")
        else:
            return self.queue[self.front]
def rear(self):
        if (self.front == self.rear):
            print("No element in the Circular Queue\n")
        else:
            return self.queue[self.rear]
def isEmpty(self):
        if (self.front == self.rear):
            return True
        else:
            return False

# Example usage:
circular_queue = circularqueue(5)
print(circular_queue.isEmpty())  # Output: True
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
print(circular_queue.front())  # Output: 1
print(circular_queue.rear())     # Output: 3
print(circular_queue.dequeue())
print(circular_queue.dequeu())
