# 숫자 타입->타입마다 사용할 수 있는 연산, 함수가 다르다
# 산술연산 : + - * / // %
num1, num2 = 10, 3.14
# + - * / 결과 출력 - 한줄로
hap = num1+num2
print(hap)
print(num1+num2)
print(f'합계 : {num1+num2}, 곱셈: {num1*num2}')
# print('합계 : {num1+num2}')

num2=3
print(f"몫 : {num1//num2}")
print(f"나머지: {num1%num2}")

print(-num1)

# 함수 : 이름을 가진 기능->재사용, 내장함수(import x)
# num1의 절대값 출력
print(abs(-5))

print(abs('aaa'))