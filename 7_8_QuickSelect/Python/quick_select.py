
def partition(vals, ib, ie):
    ip = (ib+ie)//2
    p = vals[ip]
    vals[ib], vals[ip] = vals[ip], vals[ib]
    ip = ib
    for i in range(ib+1, ie+1):
        if vals[i] < p:
            ip += 1
            vals[i], vals[ip] = vals[ip], vals[i]
    vals[ib], vals[ip] = vals[ip], vals[ib]
    return ip


def kth_smallest(k, vals, ib=0, ie=-1):
    if ie == -1:
        ie = len(vals)-1
    if ib == ie:
        return ib
    ip = partition(vals, ib, ie)
    if ip == k-1:
        return ip
    elif k-1 < ip:
        return kth_smallest(k, vals, ib, ip)
    else: # k > ip:
        return kth_smallest(k, vals, ip+1, ie)



vals = [7,3,0,1,2,9,8,6,4,5]
res = kth_smallest(3,vals)
pass