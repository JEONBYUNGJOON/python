# slicing
리스트 = [10,20,30,40,50]
# 리스트 [시작 인덱스 : 끝인덱스]
print(리스트[0:2])
print(리스트[1:4])

# slicing은 문자열도 가능
string = "0123456"
print(string[1:3])
#234
print(string[2:5])
#간격지정
print(string[3::3])
#string에서 홀수 문자를 출력
print(string[1::2])

