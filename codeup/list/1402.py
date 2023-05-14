tmp = int(input()) - 1
number = list(map(int, input().split()))

for i in range(tmp, -1, -1):
    print(number[i], end=" ")