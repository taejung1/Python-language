arr = [1, 6, 7, 8, 9, 3, 5, 4, 2]
arr_len = len(arr)

def Split(arr) :
    if len(arr) == 1 :
        return arr
    Split(arr[:len(arr)])
    Split(arr[len(arr) :])


for text in arr:
    print(text)


# for i in range(1, arr_len):
#     for j in range(i, 0, -1):
#         if arr[j] > arr[j -1] :
#             break
#         else :
#             arr[j - 1], arr[j] = arr[j], arr[j - 1] 

# Len = len(arr)
# for i in range(Len):
#     Temp = i
#     for j in range(i + 1 , Len):
#         if arr[Temp] > arr[j] :
#             Temp = j
#     arr[i], arr[Temp] = arr[Temp], arr[i]

# for i in range(arr_len) :
#     for j in range(arr_len -1 , 0 , -1) :
#         if arr[j] > arr[j -1] :
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
