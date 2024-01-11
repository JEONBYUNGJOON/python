list1 = [15,20,30,90]
# # list의 길이를 재라 -> len()x

# a=0
# for x in list1:
#     a=a+1
# print(a)

# list의 합계를 출력하시오
hap=0
for x in list1:
    hap=hap+x
    print(hap)

# list의 평균(합계/개수)을 출력하시오

hap=0
size=0
for k in list1:
    hap = hap + k     # 15 35 65 155
    size = size + 1   # 1 2 3 4
print(hap/size)
