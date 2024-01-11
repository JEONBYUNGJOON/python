# string 타입
str1='10'
str2="3.14"
str3='홀짝홀짝홀짝홀짝'
# 연산
print(str1 + str2)      # 연결 
print(str1 * 10)        # 반복
# 인덱스 연산 -> 시퀀스과 동일
print(str3[0])
print(str3[5])
# 슬라이싱(slicing) 연산 -> 시퀀스와 동일
print(str3[0:3])        # 홀짝홀
str4="72568"
print(str4[0:3])        # 725
print(str4[1:])         # 2568
print(str4[::2])        # 758

str5="0123456789"
# 홀수만 출력               13579
# 3의 배수만 출력           0369
print(str5[1::2])
print(str5[::3])

# 내장함수 : len
print(len('hello'))

# 문자열은 변경불가능(immutable <-> mutable)
str6='hello'
list6=['h','e','l','l','o']
#str6[0]='z'
list6[0]='z'

str11 = 'hello'
str11 = 'python'
print(str11)