t, m = input().split()
if int(m) - 45 < 0:
    nm = 60 + (int(m) - 45)
    nt = int(t) - 1
    if nm == 0:
        print(nt)
    else:
        print(nt, nm)
else:
    nm = int(m) - 45
    if nm == 0:
        print(t)
    else:
        print(t, nm)