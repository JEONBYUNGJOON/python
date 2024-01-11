list1 = [1,3,5]

# 10 in list : 결과가 참거짓(10이 list에 있니?)

# list의 원소를 하나씩 꺼내 item에 담는 반복문
for item in list1:
    print(item)
    
# while 종료조건
# 컨트롤c - 코드 강제종료
index = 0 
while index<3:
    print(list1[index])
    index+=1