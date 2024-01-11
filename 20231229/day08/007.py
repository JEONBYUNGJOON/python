# 1에서 10까지의 합계 : 55
result = 0
for i in range(1,11):
    result = result + i
print(result)                #55

# 1에서 10까지의 3의 배수 출력
# for i in range(1,11):
#     if i%3==0:
#         print(i)                    # 3 6 9

# for i in range(1,11):
#     if i%3!=0:
#         continue;                   # skip
#     print(i)

# 1~100사이의 3의 배수의 합계 -> 3 6 9 -> 18
result = 0
for i in range(1,11):
    if i%3==0:
        result=result+i
print(result)                # 18

# 1~100사이의 5과 7의 공배수를 출력 : 35 70
for i in range(1,101):
    if i%5==0 and i%7==0:
        print(i)

# 1~100사이의 5의 배수와 7의 배수를 출력. 공배수는 제외
for i in range(1,101):
    if i%5==0 and i%7==0:
        continue
    if i%5==0 or i%7==0:
        print(i, end=" ")  