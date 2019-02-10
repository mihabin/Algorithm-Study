import sys
string_count = int(sys.stdin.readline())
string = list(sys.stdin.readline())
res = 0
for i in range(string_count):
    res += int(string[i])
print(res)