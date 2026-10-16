def selection_sort_vooraan(a):
    
    
    n = len(a)
    
    # positie = de index van de min (of de max in het ander algoritme)
    
    for i in range(0,n,1):
        positie = i
        min = a[i]
        for j in range(i+1,n,1):
            if a[j] < min:
                positie = j
                min = a[j]
                #print(a)
          
        a[positie] = a[i]
        a[i] = min    
    print(a)

if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    selection_sort_vooraan(a)
