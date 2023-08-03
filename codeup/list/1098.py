H , W = map(int, input().split(" "));
N = int(input())

Arr = [[0 for j in range(W)] for i in range(H)]

# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

for _ in range(N) :
    I , D , X  , Y = map(int , input().split())
    
    for _ in range(I) :
        if D == 0 :
            Arr[X - 1][Y -1] = 1
            Y+=1
        elif D == 1 :
            Arr[X - 1][Y -1] = 1
            X+=1

for i in range(W) :
    for j in range(H) :
        print(Arr[i][j] , end=" ")
    print()

