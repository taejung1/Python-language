NUMBER_1, NUMBER_2 = map(int, input().split())
LIST_1 = list(i for i in range(0, NUMBER_1 + 1))

# [0,1, 2, 3, 4, 5]

temp = 0

for i in range(NUMBER_2):
    NUMBER_3, NUMBER_4 = map(int, input().split())
    temp = 0
    for j in range(NUMBER_3, NUMBER_3 + (NUMBER_4- NUMBER_3 + 1) // 2 ):  # 여기가 틀림
        TEMP_1 = LIST_1[j]
        LIST_1[j] = LIST_1[NUMBER_4 - temp]
        LIST_1[NUMBER_4 - temp] = TEMP_1
        temp += 1

for i in range(1, len(LIST_1)):
    print("{} ".format(LIST_1[i]), end="")

