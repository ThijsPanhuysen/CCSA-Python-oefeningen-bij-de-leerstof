def som_1(n: int):
    x = 0
    for i in range(1,n):
        x+=1
    print(f"x = {x} | n = {n}")
    return x
    
def som_2(n: int):
    x = 0
    for i in range(1,2*n):
        for j in range(1,n):
            x=+1
    return x
    
def som_3(n: int):
    x = 0
    for i in range(1,2*n):
        for j in range(1,n):
            for k in range(1,j):
                x=+1    
    return x
    
def som_4(n: int):
    x = 0
    for i in range(1,2*n):
        for j in range(1,n):
            for k in range(1,i):
                x=+1    
    return x

def som_5(n: int):
    x = 0
    i = n
    while i>=1:
        x +=1
        i/=2 
    return x
    
def som_6(n: int):
    x = 0
    i = n
    while i>=1:
        for j in range(1,i):
            x +=1
        i/=2 
    return x

def som_7(n: int):
    x = 0
    i = n
    while i>=1:
        for j in range(1,n):
            x +=1
        i/=2 
    return x

invoer = int(input("Geef n: "))

print(som_3(invoer))