
class Heap:
    def parent_id(i):
        return (i - 1) // 2

    def lchild_id(i):
        return 2 * i + 1

    def rchild_id(i):
        return 2 * i + 2

    def sift_up(self,i):
        assert 0 <= i < len(self), 'Wrong arg for sift_up'
        ip = Heap.parent_id(i)
        while i > 0 and ip >= 0 and self.data[ip] < self.data[i]:
            self.data[ip], self.data[i] = self.data[i], self.data[ip]
            i = ip
            ip = Heap.parent_id(i)


    def sift_down(self,i):
        assert 0<=i<len(self), 'Wrong arg for sift_down'
        while i < len(self):
            i_dn = i
            l_id = Heap.lchild_id(i)
            if l_id < len(self) and self.data[l_id] > self.data[i]:
                i_dn = l_id
            r_id = Heap.rchild_id(i)
            if r_id < len(self) and self.data[r_id] > self.data[i_dn]:
                i_dn = r_id
            if i_dn != i:
                self.data[i], self.data[i_dn] = self.data[i_dn], self.data[i]
                i = i_dn
            else:
                break


    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add(self, v):
        self.data.append(v)
        self.sift_up( len(self)-1 )

    def popmax(self):
        if not self.data:
            return None
        vmax = self.data[0]
        self.data[0] = self.data[len(self)-1]
        self.data.pop()
        self.sift_down(0)
        return vmax

    def heapify(self, arr):
        '''
        Create a heap from array. O(n)
        '''
        self.data = arr #it's not a copy, just a ref!
        istart = Heap.parent_id(len(arr)-1) # the last having any children
        for i in range(istart, -1, -1):
            self.sift_down(i)

    def is_heap(self):
        if not self.data:
            return True
        i = 0
        while True:
            l_id = Heap.lchild_id(i)
            r_id = Heap.rchild_id(i)
            if l_id >= len(self) and r_id >= len(self):
                break
            if l_id < len(self) and self.data[l_id] > self.data[i]:
                return False
            if r_id < len(self) and self.data[r_id] > self.data[i]:
                return False
            i += 1
        return True



hp = Heap()
hp.add(1)
hp.add(2)
hp.add(0)
hp.add(6)
hp.add(4)
hp.add(3)
hp.add(5)


res = hp.popmax()

arr = [1,2,0,6,4,3,5]
h1 = Heap()
h1.heapify(arr)
res = h1.is_heap()


pass



