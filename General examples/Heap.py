import math

class heap:
    def __init__(self,list=[]):
        self.list = list
        self.min = False
    def isempty(self):
        if not self.list:
            return True
        else:
            return False
    def swap(self,i1, i2):
        p1 = self.list[i1]
        p2 = self.list[i2]
        self.list[i1], self.list[i2] = p2, p1

    def siftDown(self,i):
        parent = self.list(i)
        iLchild = 2*i + 2
        iRchild = 2*i + 1
        leftChild = self.list(iLchild)
        rightChild = self.list(iRchild)
        if parent < leftChild:
            swap(i, iLchild)
        elif parent < rightChild:
            swap(i,iLchild)

    def heapify(self):
        if self.isempty():
            raise IndexError('List is empty')
        #index of root element
        i = -1
        while i < len(self.list):
            iparent = math.floor((i-1)/2)
            iLchild = 2*i + 1
            iRchild = 2*i + 2
            if self.list[iparent] < self.list[iLchild]:
                self.swap(i, iLchild)
            elif self.list[iparent] < self.list[iRchild]:
                self.swap(i,iRchild)
            
            i += 1      




def main():
    tree = heap([1,4,5,10,11,6,7])
    t = heap([5,8,7])
    #print(tree.list)
    t.heapify()
    print(t)

if __name__ == '__main__':
    main()