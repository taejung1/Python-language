NUMBER_1 , NUMBER_2 = map(int , input().split())
LIST_1 = []

for i in range(1,NUMBER_1 + 1) :
    LIST_1.append(i)

for i in range(NUMBER_2) :
    TEMP_1 , TEMP_2 = map(int,input().split())
    for j in range(NUMBER_2 // 2) :
        TEMP_3 = LIST_1[TEMP_1 + j]
        LIST_1[TEMP_1 + j] = LIST_1[TEMP_2 - j]
        LIST_1[TEMP_2 - j] = TEMP_3

for i in LIST_1 :
    print("{} ".format(i) , end="")





