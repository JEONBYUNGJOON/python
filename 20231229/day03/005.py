# 파이썬은 타입을 바꿀 수 있고 파이썬은 알아서 바꾸는 경우도 있다

# int, float, bool, str, (list, set, distion)
# 타입을 바꾸는 함수는 타입의 이름과 같다
'3'
print(int('3'))
      
# 문자 3을 정수로 바꾼 다음 타입을 확인하자
# int(), typr(), print()
print(type(int('3')))

print(3+int('3'))


# 3+'3.14'출력(6.14)
print(3+float('3.14'))

print('3'+'3')
print('5'+str(5))


print('당신은 성인입니까? '+str(True))
