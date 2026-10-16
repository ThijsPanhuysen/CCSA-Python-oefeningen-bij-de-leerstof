def sorteren_samenvoegen_omgekeerd(rij):
    
    n = len(rij)
    
    for i in range(n-2,-1,-1):
        x = rij[i]
        j = i
        while j<n-1 and x < rij[j+1]:
            rij[j] = rij[j+1]
            j += 1
        rij[j] = x
    return rij


list = [6,3,7,5,10,2,8]

print(sorteren_samenvoegen_omgekeerd(list))