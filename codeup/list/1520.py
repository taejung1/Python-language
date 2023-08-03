Number_1 , Number_2 = map(int, input().split(" "))
X_1, Y_1, Z_1 = map(int, input().split(" "))

Arr = [[0 for j in range(Number_2)] for i in range(Number_1 )]
Next_Arr = [[0 for j in range(Number_2)] for i in range(Number_1)]

for i in range(Number_1):
    Temp = input().split(" ")
    for j in range(len(Temp)):
        Arr[i][j] = int(Temp[j])

C_1 = int(input())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for C in range(C_1):
    for i in range(Number_1):
        for j in range(Number_2):
            All = 0
            for k in range(8):
                if 0 <= i + dx[k] < Number_1 and 0 <= j + dy[k] < Number_2:
                    if Arr[i+dx[k]][j+dy[k]] == 1:
                        All += 1

            for k in range(8):
                # 주위의 이웃이 y 미만이거나 z 이상이면 죽고, y 이상 z 미만이면 산다
                if 0 <= i + dx[k] < Number_1 and 0 <= j + dy[k] < Number_2:
                    if Arr[i][j] == 1 and (All < Y_1 or All >= Z_1):
                        Next_Arr[i][j] = 0
                    if Arr[i][j] == 1 and (All >= Y_1 and All < Z_1):
                        Next_Arr[i][j] = 1

for i in range(Number_1 ):
    for j in range(Number_1 ):
        print("{} ".format(Next_Arr[i][j]), end="")
    print()
