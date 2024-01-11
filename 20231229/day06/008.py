# 메뉴로 숫자를 입력받아 처리하는 프로그램 작성
# 1. 숫자 추가 2. 숫자 출력 3. 합계 4. 값으로 삭제 999. 종료
numbers = []
while True:
    print("===== 숫자 CRUD =====")
    print("1.추가 2.출력 3.합계 4.값으로 삭제 999.종료")
    select = input('메뉴 선택:')
    if select=='1':
        val = int(input('숫자 입력:'))
        numbers.append(val)
    elif select=='2':
        for number in numbers:
            print(number, end=" ")
        print()
    elif select=='3':
        print(f'합계:{sum(numbers)}')
    elif select=='4':
        value = int(input('삭제할 숫자:'))
        if value in numbers:
            numbers.remove(value)
    elif select=='999':
        print('종료')
        break