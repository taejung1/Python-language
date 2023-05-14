res = int(input())
List = list(str(res))

result = ((int(List[1]) * 10) + (int(List[0]))) * 2
# print(str(result))
if result > 100:
    temp = list(str(result))
    result = (int(temp[1]) * 10) + int(temp[2])

if result <= 50:
    print(str(result))
    print("GOOD")
else:
    print(str(result))
    print("OH MY GOD")
