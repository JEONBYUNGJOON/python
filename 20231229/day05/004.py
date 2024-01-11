리스트 = [3, 'hello', 5>3, True]
튜플 = tuple(리스트)

# CRUD
# method : 객체(파이썬을 구성하는 부품)에 소속된 함수
리스트.append(100)
리스트[0] = 리스트[0]*10
print(리스트)
del 리스트[0]
print(리스트)

# 튜플 - 읽기전용(삭제x 변경x)
