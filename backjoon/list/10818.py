list_1 = []

number, number_1 = map(int, input().split())

for i in range(number + 1):
    list_1.append(0)
for i in range(number_1):
    i_1, j_1, k_1 = map(int, input().split())
    for j in range(i_1, j_1+1, +1):
        list_1[j] = k_1

len_1 = len(list_1)
for i in range(1, len_1):
    print(list_1[i], end=" ")
