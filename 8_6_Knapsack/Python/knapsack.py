
def knapsack_mult( Weight, Items ):
    '''

    :param W:  Allowed weight
    :param Items: list of (weight, value) of items
    :return:  Value of selected items
    '''

    Value = [0]*(Weight+1)

    for W in range(1,Weight+1):
        for I in Items:
            wi, vi = I
            if W - wi >= 0 and Value[W-wi] + vi > Value[W]:
                Value[W] = Value[W-wi] + vi

    return Value[Weight]


W = 10;
Items = [ (2, 9), (6, 30), (4, 16), (3, 14)]

#Val0 = Knapsack01(W, Items)
ValM = knapsack_mult(W, Items)
#ValF = KnapsackFrac(W, Items)

pass