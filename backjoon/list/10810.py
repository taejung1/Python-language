tmp = int(input())
number = list(map(int , input().split()))
mx = max(number)
sum_1 = 0
for i in range(tmp) :
    sum_1+=number[i] / mx * 100
print(sum_1 / tmp)
    