# functie returned de index van het gezochte item, default -1


def zoek_binair(zoekItem,rij):
    
    l=0
    r= len(rij) -1 # 9
    
    while l != r:
        m = (l+r)//2
        if rij[m] < zoekItem:
            l = m+1
        else:
            r = m
    if rij[l] == zoekItem:
        index = l
    else:
        index = -1
    return index


index = zoek_binair(70, [0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"index = {index}")
