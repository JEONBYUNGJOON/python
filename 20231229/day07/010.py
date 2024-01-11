numbers = [100,300,500,700]
# 위치를 입력 : 2       del numbers[2]

# 값을 입력받아 위치를 찾아서 삭제
value = 300 

index = 0
for num in numbers:
    if value==num:
        print(index)            # 2
    index=index+1