t =  int(input())

def tong(n):
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    if s % 10 == 0:
        return True
    return False
        
def check(n):
    for i  in range(0, len(n)- 1):
        if(abs(int(n[i]) - int(n[i + 1])) != 2):
            return False
    return True

for _ in range (t):
    n = input()
    if check(n) and tong(n):
        print("YES")
    else :
        print("NO")    