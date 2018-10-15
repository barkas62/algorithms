
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

# no repetition of items
def knapsack_01( Weight, Items ):

    # Value [i][w] : max value attainable for w knapsack, using 1...i items
    Value = [ [0]*(len(Items)+1) ] * (Weight+1)

    for i in range(1,len(Items)+1):
        wi, vi = Items[i-1]
        for w in range(1, Weight+1):
            Value[w][i] = Value[w][i-1] # w-knapsack value if it does not holds i-th item
            if wi <= w: # w-knapsack can hold i-th item
                newV = Value[w][i-1] + vi  # this would be w-knapsack value if it indeed holds i-th item
                if Value[w][i] < newV:
                    Value[w][i] = newV
    return Value[Weight][len(Items)]


W = 10;
Items = [ (2, 9), (6, 30), (4, 16), (3, 14)]
#Items = [(7,1)]
Val0 = knapsack_01(W, Items)
ValM = knapsack_mult(W, Items)
#ValF = KnapsackFrac(W, Items)

pass