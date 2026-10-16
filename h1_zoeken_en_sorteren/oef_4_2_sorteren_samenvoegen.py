def merge_sort(rij):
    
    n = len(rij) 
    
    merge_recursief(rij,0,n-1)
    return rij
    
    
def merge_recursief(rij,begin,einde):
    
    if begin < einde:
    
        midden = (begin+einde) // 2
    
        merge_recursief(rij,begin,midden) # de linkerhelft wordt gesorteerd
        merge_recursief(rij,midden+1,einde) # de rechterhelft wordt gesorteerd
        merge(rij,begin,midden,einde)
    
def merge(rij, begin, midden, einde):
    
    i = begin
    j = midden+1
    hulp_rij = [0] * len(rij)
    k = i
    
    while i<=midden and j<=einde:
        if rij[i] >= rij[j]:
            hulp_rij[k] = rij[i]
            i+=1
        else:
            hulp_rij[k] = rij[j]
            j+=1
        k+=1    
    if i>midden:
        while j<=einde:
            hulp_rij[k] = rij[j]
            j+=1
            k+=1
    else:
        while i<=midden:
            hulp_rij[k] = rij[i]
            i+=1
            k+=1
    for teller in range(begin, einde+1):
        rij[teller] = hulp_rij[teller]
    

list = [5,7,3,8,4,9,14]

print(merge_sort(list))
    
    