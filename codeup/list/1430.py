NUMBER_1 = int(input())
LIST_1 = list(map(int, input().split()))
NUMBER_2 = int(input())
LIST_2 = list(map(int, input().split()))

for i in LIST_2 :
    if i in LIST_1 :
        print("1 " , end="")
    else :
        print("0 " , end="")