res = input()
hour = int(res.split(" ")[0])
minute = int(res.split(" ")[1])

if minute >= 45:
    print("{} {}".format(hour, minute - 45))
elif hour == 0 :
    print("{} {}".format(23, minute + 15))
else:
    print("{} {}".format(hour - 1, minute + 15))
