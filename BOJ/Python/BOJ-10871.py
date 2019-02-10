a, b = input().split()
a = int(a); b = int(b)
d = []
res = ""
c = input().split()
c = list(c)
for i in range(a):
    if int(c[i]) < b:
        res += c[i]+" "
res = res[:-1]
print(res)