NUMBER_1 = int(input())
LIST_1 = list(map(int, input().split()))

# for i in range(NUMBER_1):
#     for j in range(i , NUMBER_1 + i):
#         print("{} ".format(LIST_1[j % NUMBER_1]), end="")
#     print()

# for i in range(NUMBER_1):
#     for j in range(i , i + NUMBER_1 , +1) :
#         if j >= NUMBER_1 :
#             print("{} ".format(LIST_1[NUMBER_1 - j]) , end="")
#         else :
#             print("{} ".format(LIST_1[j]) , end="")
#     print()
    
# for i in range(NUMBER_1):
#     for j in range(NUMBER_1):
#         print("{} ".format(LIST_1[i + j - NUMBER_1]), end="")
#     print()

# for i in range(NUMBER_1):
#     for j in LIST_1:
#         print("{} ".format(j), end="")
#     print()
#     TEMP = LIST_1[0]
#     for n in range(NUMBER_1 - 1):
#         LIST_1[n] = LIST_1[n+1]
#     LIST_1[NUMBER_1 - 1] = TEMP
