a, b = map(int , input().split())
TEMP = (90 - a) // 5
if a + (TEMP * 5) == 90 :
    print(TEMP + b)
else :
    print(TEMP + b+1)
