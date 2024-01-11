# 75, 80, 70이라는 국어 점수가 있다 -> 집합 타입(sequence)
# 값 하나를 저장 : int, float, str, bool
# 값 여러개를 저장 : list, tuple, dictionary, set
# 한반 학생들의 성적
kor1=75
kor2=80
kor3=70
print(kor1)
print(kor2)
print(kor3)

kor=[75,80,70]
# kor의 타입 출력
print(type(kor))
print(kor[0])
print(kor[1])
print(kor[2])

# 조건문, 반복문
#kor 리스트의 원소를 하나씩 꺼내서 item에 담는다
for item in kor:
    print(item)

리스트 = ["사과", "귤", "수박"]
튜플 = ("사과", "귤", "수박")

# Create Read Update Delete

# 리스트, 튜플 print 하세요
for qt in 리스트:
    print(qt)