"""
1.
N children come to party.
Organize into min possible groups such that
the age of any two children in the same group differ by at most 1 year
"""
def children_groups(ages: list)->int:
    """
    :param ages: list of children's ages
    :return: number of groups
    """
    n_groups = 0
    ages.sort()
    while ages:
        n_groups += 1
        max_age = ages[-1]
        ages.pop()
        while ages and max_age - ages[-1] <= 1:
            ages.pop()
    return n_groups

"""
2.
A car can travel L miles with full tank.
n gas stations on the road between A and B |AB| = dist. 
X1,...Xn-1: distances between stations.
X0 : dist between A and first station
Xn : dist between last station and A
Find min stops 
"""
def car_stops(L: int, X: list):
    if L < X[0]:
        return -1
    dist = 0
    for i, x in enumerate(X):
        dist += x
        if dist > L:
            more_stops = car_stops(L, X[i:])
            if more_stops == -1:
                return -1
            return 1 + more_stops
    return 0

"""
3.
We have a set S= { [Si, Fi), i = 0...n-1 } of n activities,
i-th activity has a start time Si, and finish time Fi.
Select a max-size subset  of non-overlapping activities.
"""
def max_activities(Activities):
    Activities.sort(key=lambda x: x[1])
    max_set = [0]
    stop_last = Activities[0][1]
    for i in range(1,len(Activities)):
        act = Activities[i]
        if act[0] >= stop_last:
            max_set.append(i)
            stop_last = act[1]
    return max_set

"""
4.
We have a set of activities to schedule among a large number of lecture halls.
We want to use as few lecture halls as possible.
"""
def used_halls(Activities):
    events = []
    for a in Activities:
        events.extend([('s', a[0]), ('f', a[1])])
    events.sort(key=lambda x: x[1])
    available = 0   # available halls
    n_used = 0
    for e in events:
        if e[0] == 's':
            if not available:
                n_used += 1
            else:
                available -= 1
        elif e[0] == 'f':
            available += 1
    return n_used



if __name__ == "__main__":
    ages = [5.1, 5.5, 7, 7, 3, 3.3, 4]
    n_groups = children_groups(ages)

    L = 20
    X = [1, 2, 7, 11, 20, 20]
    n_stops = car_stops(L, X)
    X = [1, 2, 7, 11, 21, 20]
    n_stops = car_stops(L, X)
    pass



