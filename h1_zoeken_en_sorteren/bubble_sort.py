def bubble_sort(a):
    
    n = len(a)
    counter = 0
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                
                x = a[j]
                y = a[j-1]
                
                a[j] = y
                a[j-1] = x
            print(a)
            counter +=1
    return counter

if __name__ == "__main__":
    a = [int(_) for _ in input().split()]
    counter = bubble_sort(a)
    n = len(a)
    print(a)
    print(f"Voor een rij van lengte {n} werd het if statement {counter} keer uitgevoerd.")
    
    
#1. Buitenste lus (for i in range(n - 1)): Bepaalt hoeveel keer de lijst doorlopen wordt.
#2. Binnenste lus (for j in range(n - i - 1)): Vergelekt steeds twee naast elkaar liggende elementen (arr[j] en arr[j + 1]).


#formule = n(n-1) / 2