# 초를 입력받고 분으로 나타내는 프로그램을 작성하시오
a = int(input())
mins = a/60
sec = a%60
print("{}분 {}초".format(int(mins), sec))
