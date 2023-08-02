Num_1 = int(input())
Arr = [[0 for j in range(100)] for i in range(100)]

for i in range(Num_1):
    Num_2, Num_3 = map(int, input().split(" "))

    for j in range(Num_2, Num_2 + 10):
        for k in range(Num_3, Num_3 + 10):
            Arr[j][k] = 1

Total = 0
for i in range(100):
    for j in range(100):
        if Arr[i][j] == 1:
            Total += 1
print(Total)

