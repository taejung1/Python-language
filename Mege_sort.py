arr = [1, 6, 7, 8, 9, 3, 5, 4, 2]
arr_len = len(arr)


def Split(arr):
    if len(arr) <= 1:
        return arr
    arr_len = len(arr)
    left = Split(arr[:arr_len // 2])
    right = Split(arr[arr_len // 2:])

    return Merge(left , right) 

def Merge(left , right) :
    List = []

    while 1 :
        if left[0] > right[0] :
            List.append( right[0])
            List.append( left[0])



Split(arr)



# for text in arr:
#     print(text)


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
