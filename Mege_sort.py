arr = [7,9,2,1,4,6,5,3,9,3]
arr_len = len(arr)


def Split(arr):
    if len(arr) <= 1:
        return arr
    arr_len = len(arr)
    left = Split(arr[:arr_len // 2])
    right = Split(arr[arr_len // 2:])

    return Merge(left, right)


def Merge(left, right):  # 7 9 
    arr_temp = []

    i_1 , j_1 = 0 , 0 

    while i_1 < len(left) and j_1 < len(right) :
        if left[i_1] < right[j_1] :
            arr_temp.append(left[i_1])
            i_1 += 1
        else :
            arr_temp.append(right[j_1])
            j_1 += 1

    while i_1 < len(left) :
        arr_temp.append(left[i_1])
        i_1 += 1

    while j_1 < len(right) :
        arr_temp.append(right[j_1])    
        j_1 += 1

    return arr_temp

print(Split(arr))


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
