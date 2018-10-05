
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
    def __init__(self, data, parent = None):
        self.parent   = parent
        self.children = []
        self.data     = data

    def addChild(self, childNode):
        if childNode is not None:
            self.children.append(childNode)
            childNode.parent = self

class Tree():
    def __init__(self):
        self.root = None

    def add(self, data, parentNode=None):
        newNode = TNode(data)
        if parentNode is not None:
            parentNode.addChild(newNode)
        elif self.root is None:
            self.root = newNode
        else:
            raise Exception('Bad parent node provided')

        return newNode

    def __iter__(self):
        stack = [self.root]
        while len(stack):
            node = stack.pop()
            yield node.data
            stack.extend( reversed(node.children))

    def _dfs(self, node, datalist, order = 'preorder'):
        if order == 'preorder':
            datalist.append(node.data)
        for i,child_node in enumerate(node.children):
            self._dfs(child_node, datalist)
            if order == 'inorder' and i != len(node.children)-1:
                datalist.append(node.data)
        if order == 'postorder':
            datalist.append(node.data)

    def _dfs_iter(self, node, datalist):
        stack = [self.root]
        while len(stack):
            node = stack.pop()
            datalist.append(node.data)
            for child_node in reversed(node.children):
                stack.append(child_node)



    def _bfs(self, node, datalist):
        queue = [node]
        while len(queue):
            node = queue.pop(0)
            datalist.append(node.data)
            for child_node in node.children:
                queue.append(child_node)


    def traverse(self, method = 'dfs', order="postorder"):
        dataList = []
        if method == 'dfs':
            self._dfs(self.root, dataList, order)
        else:
            self._bfs(self.root, dataList)
        return dataList


T = Tree()
rootNode = T.add('1')
node11 = T.add('11', rootNode)
node12 = T.add('12', rootNode)
node111 = T.add('111', node11)
node112 = T.add('112', node11)
node1111 = T.add('1111', node111)

datalist_pre = T.traverse('dfs', 'preorder')
datalist_in = T.traverse('dfs', 'inorder')
datalist_post = T.traverse('dfs', 'postorder')
#datalist = list( x for x in T)

pass