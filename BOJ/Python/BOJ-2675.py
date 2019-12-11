sl = []
t = int(input())
for i in range(t):
    n, s = input().split()
    sl.append((n, s))
for i in range(len(sl)):
    for j in sl[i][1]:
        print(j * int(sl[i][0]), end='')
    print()