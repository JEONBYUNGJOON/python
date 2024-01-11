# break : 반복문을 중단한다
while True:
    a = int(input('값을 입력하시오(999면 종료)'))
    if a==999 : 
        break
    print(f'입력한 값 : {a}')
    