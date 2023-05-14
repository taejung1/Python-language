import copy

n = int(input())
tmp = n

i = 1
while True :
    n = (n % 10) * 10 + ( n // 10 + n % 10 ) % 10
    if n == tmp :
        print(i)
        break
    i+=1
