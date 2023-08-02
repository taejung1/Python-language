Arr = [[0 for j in range(25)] for i in range(25)]

for i in range(25):
    Temp = input().split(" ")
    for j in range(24):
        Arr[i][j] = int(Temp[j])


def find(X, Y):
    number = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if X + i >= 0 and Y + j >= 0 and X + i <= 24 and Y + j <= 24 and X != 0 and Y != 0:
                if Arr[X+i][Y+j] == 1:
                    number += 1
    return number


for i in range(25) :
    for j in range(25) :
        call = find(i, j);
        a = call;
        d = 8 - call;

        if Arr[i][j] == 0 and a == 3 :
            Arr[i][j] = 1;
        if Arr[i][j] == 0 and (a >= 4 or a <= 1) :
            Arr[i][j] = 0;
        if Arr[i][j] == 1 and (a ==2 or a==3) :
            Arr[i][j] = 1;

for i in range(25) :
    for j in range(25) :
        print("{} ".format(Arr[i][j]) ,end="")
    print()
         