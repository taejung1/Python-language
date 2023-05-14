NUMBER_1, NUMBER_2 = map(int, input().split())
LIST_1 = list(i + 1 for i in range(0, NUMBER_1))

for index in range(NUMBER_2):
    INPUT_1, INPUT_2, INPUT_3 = map(int, input().split())
    LIST_1 = LIST_1[:INPUT_1 - 1] + LIST_1[INPUT_3 - 1: INPUT_2] + \
        LIST_1[INPUT_1 - 1: INPUT_3 - 1] + LIST_1[INPUT_2:]

for I in LIST_1:
    print("{} ".format(I), end="")
