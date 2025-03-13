s = input()
a = 0
b = 0

for i in range (len(s)):
    if(s[i].islower()): a += 1
    if(s[i].isupper()): b += 1
if a >= b : print(s.lower())
else: print(s.upper())