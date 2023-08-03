Arr = [[0 for j in range(25)] for i in range(25)]
Next_Arr = [[0 for j in range(25)] for i in range(25)]

for i in range(25):
    Temp = input().split(" ")
    for j in range(25):
        Arr[i][j] = int(Temp[j])

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(25):
    for j in range(25):
        All = 0
        for k in range(8):
            if 0 <= i + dx[k] <= 24 and 0 <= j + dy[k] <= 24:
                if Arr[i+dx[k]][j+dy[k]] == 1:
                    All += 1

        for k in range(8):
            if 0 <= i + dx[k] <= 24 and 0 <= j + dy[k] <= 24:
                if Arr[i][j] == 0 and All == 3:
                    Next_Arr[i][j] = 1
                if Arr[i][j] == 1 and (All >= 4 or All <= 1):
                    Next_Arr[i][j] = 0
                if Arr[i][j] == 1 and (All == 2 or All == 3):
                    Next_Arr[i][j] = 1

for i in range(25):
    for j in range(25):
        print("{} ".format(Next_Arr[i][j]) , end="")
    print()
