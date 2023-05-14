NUMBER_1 , NUMBER_2 = map(int, input().split())
LIST_1 = list(map(int,input().split()))
LIST_1.sort()
TMP = 0
for i in range(NUMBER_1) :
    if TMP == NUMBER_2 :
        print()
        TMP = 0 
    print("{} ".format(LIST_1[i]) , end="")
    TMP +=1