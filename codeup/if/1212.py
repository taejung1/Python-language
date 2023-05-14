a, b, c = map(int, input().split())

Max = max(a,b,c)
tmp = a + b + c - Max

if Max < tmp :
    print("yes")
else :
    print("no")
