a , b = map(int , input().split())

last_day2 = [31,22,31,30,31,30,31,31,30,31,30,31]

if b == 2 :
    if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0) :
        print(29)
    else :
        print(28)
else :
    print(last_day2[b - 1])