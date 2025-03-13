import math

def nto(n):
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    dao = 0
    s = 0
    temp = n
    while(n > 0):
        k = n % 10
        if nto(k) == False : return False
        dao = dao * 10 + k
        s += k
        n = int(n /10)
    if nto(dao) and nto(temp) and nto(s): return True
     

t = int(input())
for i in range (t):
    n = int(input())
    if check(n) == True:
        print("Yes")
    else:
        print("No")