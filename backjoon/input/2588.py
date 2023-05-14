a = int(input())
b = int(input())

List = list(str(b))

#첫번쨰 출력
print(a * int(List[int(len(List)) - 1]))
#두번쨰 출력
print(a * int(List[int(len(List)) - 2]))
#3번째 출력
print(a * int(List[int(len(List)) - 3]))
#마지막 출력
print(a * b)