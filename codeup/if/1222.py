a, b, c = map(int, input().split())
TEMP = (90 - a) // 5
TMP = 0
if a + (TEMP * 5) == 90:
    TMP = TEMP 
else:
    TMP = TEMP + 1

if TMP + b > c:
    print("win")
elif TMP + b == c:
    print("same")
else:
    print("lose")
