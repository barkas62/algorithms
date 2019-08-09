from random import randint


class HashOpenAddr:
    mers_prime = (2 << 13) - 1
    DELETED = '_<deleted>_'
    def __init__(self, size = 1024):
        self.arr = [None]*size
        self.size = size
        self.used = 0

        h = []
        for i in [1,2]:
            a = randint(1, HashOpenAddr.mers_prime)
            b = randint(1, HashOpenAddr.mers_prime)
            h.append( lambda x:(((a*x)%HashOpenAddr.mers_prime + b)%HashOpenAddr.mers_prime) % self.size )

        self.hash = lambda key, it: (((h[0](key)*it) % HashOpenAddr.mers_prime + h[1](key))
                                     % HashOpenAddr.mers_prime) % self.size

    def put(self, key):
        assert key != HashOpenAddr.DELETED, Exception('Bad key')
        for it in range(self.size):
            i = self.hash(key, it)
            if self.arr[i] is None or self.arr[i] == HashOpenAddr.DELETED:
                self.arr[i] = key
                self.used += 1
                break
            if self.arr[i] == key:
                break
        else:
            raise Exception('Table is full')

    def __contains__(self, key):
        assert key != HashOpenAddr.DELETED, Exception('Bad key')
        for it in range(self.size):
            i = self.hash(key, it)
            if key == self.arr[i]:
                return True
        return False

    def remove(self, key):
        assert key != HashOpenAddr.DELETED, Exception('Bad key')
        for it in range(self.size):
            i = self.hash(key, it)
            if key == self.arr[i]:
                self.arr[i] = HashOpenAddr.DELETED
                break
        else:
            raise Exception('Key not found')


hash = HashOpenAddr(16)

for i in range(10):
    hash.put(i)


for key in range(10):
    if key in hash:
        hash.remove(key)

pass







