import sys

def change_money_dp( amount, Coins ):
    n_change = [1<<31]*(amount+1) #count change
    c_change = [0]*(amount+1)     # coin values for backprop
    n_change[0] = 0
    for amt in range(1, amount+1):
        for coin_value in Coins:
            if amt - coin_value >= 0:
                if n_change[amt] > n_change[amt-coin_value] + 1:
                    n_change[amt] = n_change[amt-coin_value] + 1
                    c_change[amt] = coin_value

    change = []
    amt = amount
    while amt:
        change.append(c_change[amt])
        amt -= c_change[amt]

    return n_change[amount], change

def change_money_memoization( amount, Coins, n_change):
    if not amount:
        return 0

    for coin_value in reversed(Coins):
        amt = amount - coin_value
        if amt >= 0:
            if n_change[amt] == (1<<31):
                n_change[amt] = change_money_memoization( amt, Coins, n_change)
            else:
                pass
            if n_change[amount] > n_change[amt] + 1:
                n_change[amount] = n_change[amt] + 1

    return n_change[amount]

Coins = [3,5,10,20,25,50]
amount = 4

#n_coin, change = change_money_dp(amount,Coins)

n_change = [1<<31]*(amount+1)
n_coin = change_money_memoization(amount,Coins, n_change)

pass

