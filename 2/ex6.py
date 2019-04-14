class Queue:
    myList = list()

    def __init__(self, start):
        self.myList.append(start)

    def enqueue(self, data):
        self.myList.append(data)


    def dequeue(self):
        if self.isEmpty():
            return None

        return self.myList.pop(0)
   
    def isEmpty(self):
        if not self.myList:
            return True
        return False





start = {'T': []}
mQ = Queue(start)
print(mQ.myList)
