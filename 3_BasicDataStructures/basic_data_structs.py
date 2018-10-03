
from functools import reduce
import operator

# Array : 'list' or array
# But lst can contain items ov diff size. array hold items of same size

# Initializing

a = [1,2,'any', 5.]       # any objects
a[1] = [1.1, 1.2, 1.3]    # replacing second element with the list

b = [ i**2 for i in range(5) if i%2 ]  # comprehension, produces [1, 4]
c = ( i**2 for i in range(5) if i %2 ) # generator expression, same as above, but takes less memory


#============================================

# Linked list
class LLnode():
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def add(self, node):
        self.next = node

class LinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode is not None:
            yield curNode.data
            curNode = curNode.next

    def __str__(self):
        """
        Prints the current list in the form of a Python list
        """
        return str(list(self))

    def getTail(self):
        if self.head is None:
            return None
        curNode = self.head
        while curNode.next is not None:
            curNode = curNode.next
        return curNode

    def append(self, data):
        newNode = LLnode(data)
        tailNode = self.getTail()
        if tailNode is not None:
            tailNode.add( newNode )
        else:
            self.head = newNode

    def prepend(self, data):
        newNode = LLnode(data)
        oldHead = self.head
        self.head = newNode
        if oldHead is not None:
            self.head.next = oldHead

    def size(self):
        n = reduce(lambda x,y: x+1,self,0)  # self is iterable : __iter__ is provided


myList = LinkedList()
myList.append(2)
myList.prepend(1)
myList.append(3)

nsize = myList.size()

for data in myList:
    print(str(data))
    for data1 in myList:
        print ('----'+ str(data1))

print(myList)


#===========   Tree =======================


class TNode():
    def __init__(self, data, parent):
        self.parent   = parent
        self.children = list()
        self.data     = data

    def addChild(self, childNode):
        if childNode is not None:
            self.children.append(childNode)
            childNode.parent = self

class Tree():
    def __init__(self):
        self.root = None

    def add(self, data, parentNode=None):
        newNode = TNode(data, parentNode)
        if parentNode is not None:
            parentNode.addChild(newNode)
        elif self.root is None:
            self.root = newNode
        else:
            raise Exception('Bad parent node provided')

        return newNode

T = Tree()
rootNode = T.add(0)
node01 = T.add('0-1', rootNode)
node02 = T.add('0-2', rootNode)
node13 = T.add('1-3', node01)


pass