import sys
string = input()
string_num = int(len(string)/10)
nownum = 0
for i in range(string_num):
    print(string[nownum:nownum + 10])
    nownum += 10
if len(string) - (string_num*10) > 0:
    print(string[string_num*10:])