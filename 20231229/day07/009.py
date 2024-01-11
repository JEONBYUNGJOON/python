# 숫자 리스트 - 추가, 목록, 변경, 삭제. 함수버전 
numbers=[1,3,5]

def print_menu():
    print('############## 숫자 CRUD ###############')
    print('1:추가, 2:목록, 3:삭제, 999:종료')

def input_select():
    return input('메뉴 선택:')

def add_value():
    value = int(input('값 입력:'))
    numbers.append(value)

def list_numbers():
    for num in numbers:
        print(num, end=" ")
    print()

def delete_number() :
    value = int(input('삭제할 값 입력')) 
    index = 0
    for num in numbers:
        if num==value:
           del numbers[index]
        index=index+1

while True:
    print_menu()
    select = input_select()
    if select=='1':
        add_value()
    elif select=='2':
        list_numbers()
    elif select=='3':
        delete_number()
    elif select=='999':
        break