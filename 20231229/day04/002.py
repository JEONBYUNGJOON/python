a ='345'
b = int(a) # 345
c = float(a) # 345.0
d = str(b) # '345'

ar = [30,40,50]
# ar을 튜플로 변환해 br에 저장하시오
br = tuple(ar)

# 리스트에 원소를 추가한다 : append
# .은 멤버 연산자
# append는 프리랜서가 아니라 ar에 소속된 홤수 -> method

ar.insert(2,45)
print(ar)


xr = (10,20,30)
# xr에 40을 추가한 다음 출력하시오
xr = list(xr)
xr.append(40)
xr = tuple(xr)
print(xr)

