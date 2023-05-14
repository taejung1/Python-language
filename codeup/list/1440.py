NUMBER_1 = int(input())
LIST_1 = list(map(int, input().split()))
for i in range(NUMBER_1):
    TMP = ""
    print("{}:".format(i + 1) , end=" ")
    for j in range(NUMBER_1):
        if i != j :
            if LIST_1[i] < LIST_1[j]:
                print("<", end=" ")
            elif LIST_1[i] > LIST_1[j]:
                print(">", end=" ")
            elif LIST_1[i] == LIST_1[j]:
                print("=", end=" ")
    print()
