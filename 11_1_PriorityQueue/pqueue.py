import heapq
from collections import defaultdict
from time import time

class PQueueMax:
    class Entry:
        def __init__(self, priority, counter, task):
            self.priority = priority
            self.counter  = counter
            self.task = task

        def __lt__(self, other):
            if self.priority < other.priority:
                return False
            elif self.priority == other.priority:
                return self.counter < other.counter
            else:
                return True

    def __init__(self):
        self.pq = []  # all entries
        self.entry_map = defaultdict(dict)  # task : entry map

    def __len__(self):
        return len(self.pq)

    def push(self, task, priority):
        counter = time()
        entry = PQueueMax.Entry(priority, counter, task)
        self.entry_map[task][counter] = entry
        self.counter += 1
        heapq.heappush(self.pq, entry)

    def pop(self):
        while self.pq:
            entry = heapq.heappop(self.pq)
            if entry.task is None:
                continue
            tasks_dict = self.entry_map[entry.task]
            del tasks_dict[entry.counter]
            return entry.task
        raise IndexError('Empty queue')

    def remove(self, task):
        if task not in self.entry_map:
            return
        tasks_dict = self.entry_map[task]
        for entry in tasks_dict.values():
            entry.task = None
        del self.entry_map[task]


pqm = PQueueMax()
pqm.push('task1', 5)
pqm.push('task2', 5)
pqm.push('task2',10)
pqm.push('task3', 1)

#pqm.remove('task2')

task1 = pqm.pop()
task2 = pqm.pop()
task3 = pqm.pop()
task4 = pqm.pop()
task5 = pqm.pop()

pass


