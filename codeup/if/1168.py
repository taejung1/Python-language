a , b = map(int , input().split())


m = a // 10000

y = 0
if b == 1 or b == 2 :
    y+= 1900
else :
    y+= 2000

print(2012 - (y + m) + 1 )