string = input()
stringlist = list(string)
res = ""
count = 0
for i in range(len(stringlist)):
    if count == 10:
        res += "\n"
        count = 0
    count += 1
    res = res + stringlist[i]
print(res)