NUMBER_1 = int(input())
LIST_1 = []
for i in range(NUMBER_1):
    LIST_1.append(int(input()))
COUNT = 1
LEN_1 = NUMBER_1 - 1
MAX_1 = LIST_1[LEN_1]

for i in range(LEN_1 -1 , -1 , -1):
    if LIST_1[i] > MAX_1:
        COUNT += 1
        MAX_1 = LIST_1[i]

print(COUNT)