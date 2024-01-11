member = []
member.append("권충만")
member.append("김영진")
member.append("김준엽")
member.append("김채린")
member.append("백하나")
member.append("봉혜빈")
member.append("서준우")
member.append("이종모")
member.append("이하은")
member.append("이호웅")
member.append("전병준")
member.append("정태민")
member.append("정현우")
member.append("조민재")
member.append("조정빈")
member.append("진현석")
member.append("최민기")
member.append("최현선")
member.append("한지헌")
member.append("황석원")
member.append("황현성")

member2= ['류동하','안재휴','홍유빈','황규민']

import random
random.shuffle(member)
random.shuffle(member2)

print("====== 1조 =====")
print(member[0:4], end=" ")
print(member2[0])

print("====== 2조 =====")
print(member[4:8], end=" ")
print(member2[1])

print("====== 3조 =====")
print(member[8:12], end=" ")
print(member2[2])

print("====== 4조 =====")
print(member[12:16], end=" ")
print(member2[3])

print("====== 5조 =====")
print(member[16:21])