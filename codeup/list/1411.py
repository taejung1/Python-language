n = int(input())
list_1 = []

for i in range(n + 1) :
    list_1.append(0)

for i in range(n -1) :
    tmp = int(input())
    list_1[tmp] = 1

Len = len(list_1)
for i in range(Len) :
    if list_1[i] == 0 and i != 0 :
        print(i)