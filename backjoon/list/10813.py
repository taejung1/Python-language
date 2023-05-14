NUMBER_1, NUMBER_2 = map(int, input().split(" "))
LIST_1 = list(i for i in range(1, NUMBER_1 + 1))
for i in range(1, NUMBER_2 + 1):
    TMP_1, TMP_2 = map(int, input().split(" "))
    TMP_3 = LIST_1[TMP_1 - 1]
    LIST_1[TMP_1 - 1] = LIST_1[TMP_2 -1]
    LIST_1[TMP_2 - 1] = TMP_3
for i in range(0, NUMBER_1):
    print(LIST_1[i], end=" ")
