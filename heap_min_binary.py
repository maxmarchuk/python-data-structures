import math

class BinaryMinHeap(object):
    def __init__(self, fromList=None):
        if fromList is None:
            self.heapList = [0]
            self.currentSize = 0;
        else:
            # set starting point from middle of the list because
            # we know all of its children will be leaves
            i = len(fromList) // 2
            self.currentSize = len(fromList)
            self.heapList = [0] + fromList[:] # shallow copy new list
            while i > 0:
                self.bubbleDown(i)
                i -= 1

    def insert(self, num):
        self.heapList.append(num);
        self.currentSize += 1
        self.bubbleUp(self.currentSize)

    def extractMin(self):
        minValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.bubbleDown(1)
        return minValue

    def bubbleUp(self, i):
        # "//" is floor division (same as `math.floor( i / 2)`)
        while i // 2 > 0: # stop if we're at the top of the heap
            parent = i // 2 # calculate parent index
            if(self.heapList[i] < self.heapList[parent]):
                tmp = self.heapList[parent]
                self.heapList[parent] = self.heapList[i]
                self.heapList[i] = tmp
            i = parent
    
    def bubbleDown(self, i):
        while i *  2 <= self.currentSize: # stop if we're at the bottom of the heap
            minChild = self.minChildOf(i)
            if self.heapList[i] > self.heapList[minChild]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[minChild]
                self.heapList[minChild] = tmp
            i = minChild

    def minChildOf(self, i):
        if i*2+1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def heapSort(self):
        tmpHeap = BinaryMinHeap(self.heapList[1:])
        sorted = []
        while tmpHeap.currentSize > 0: 
            sorted.append(tmpHeap.extractMin())
        print("Sorted List: ", sorted)

    def print(self):
        print("List: {}".format(self.heapList[1:]))
        level = 1
        for i in range(1, self.currentSize+1):
            x = math.log(i, 2) % 2
            if x == 0 or x == 1:
                print("-- Level {} --".format(level))
                level += 1
            print("{}:\t{}".format(i, self.heapList[i]))

