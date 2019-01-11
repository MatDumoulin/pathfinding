# A basic FIFO queue implementation.
# It basically wraps an array to restrain its public methods for queue usage only.
class Queue:
    def __init__(self):
        self.values = []

    def __len__(self):
        return len(self.values)
    
    def append(self, value):
        self.values.append(value)

    def appendQueue(self, otherQueue):
        self.values = self.values + otherQueue.values
    
    def pop(self):
        return self.values.pop(0)

    # The ends becomes the beginning
    def reverse(self):
        self.values.reverse()

    def asList(self):
        return self.values.copy()

    def __str__(self):
        return ' '.join(str(x) for x in self.values)
