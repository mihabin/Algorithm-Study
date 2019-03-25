mon, day = input().split()
mon = int(mon); day = int(day)
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = 0
for i in range(mon-1):
    res += months[i]
res += day
res = res%7
if res == 1:
    print("MON")
elif res == 2:
    print("TUE")
elif res == 3:
    print("WED")
elif res == 4:
    print("THU")
elif res == 5:
    print("FRI")
elif res == 6:
    print("SAT")
elif res == 0:
    print("SUN")