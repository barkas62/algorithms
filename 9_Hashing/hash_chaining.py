import random

class ListNode:
    def __init__(self, key, val, next = None):
        self.next = next
        self.key = key
        self.val = val


class HashMap:
    mers_prime = (2<<13) - 1

    def __init__(self, size = 1024):
        self.items_count = 0
        self.size = size
        self.arr = [None]*size
        self.hash_a = random.randint(1, HashMap.mers_prime)
        self.hash_b = random.randint(1, HashMap.mers_prime)
        self.hash = lambda x: (((self.hash_a*x)%HashMap.mers_prime + self.hash_b)%HashMap.mers_prime)%size

    def put(self, key, val):
        chain_id = self.hash(key)
        prv_head = self.arr[chain_id]
        self.arr[chain_id] = ListNode(key, val, prv_head)
        self.items_count += 1

    def get(self, key):
        chain_id = self.hash(key)
        cur_node = self.arr[chain_id]
        while cur_node:
            if cur_node.key == key:
                return cur_node.val
        return None

    def delete(self, key):
        chain_id = self.hash(key)
        prv_node = None
        cur_node = self.arr[chain_id]
        while cur_node:
            if cur_node.key == key:
                if prv_node:
                    prv_node.next = cur_node.next
                else:
                    self.arr[chain_id] = cur_node.next
                return
            prv_node = cur_node
            cur_node = cur_node.next



hm = HashMap(8)

hm.put(1,'one')
r1 = hm.get(1)

hm.put(2,'two')
hm.put(3,'three')

r2 = hm.get(2)
r_ = hm.get(0)

pass









