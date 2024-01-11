# 할일 관리
todos=[
    {'tno':1, 'title':'할일 1', 'reg_day': '2024-01-09', 'finish':False},
    {'tno':3, 'title':'할일 3', 'reg_day': '2024-01-09', 'finish':False}
]
tno=2
# Read : 전체읽기, 1개일기
for todo in todos:
    print(todo)

    # 할일 번호를 입력받아 찾아서 출력
    input_tno = int(input('할 일 번호 입력:'))
    찾았니 = False
    for todo in todos:
        if todo['tbo']==input_tno:
            print(todo)
            찾았니 = True
            break
if 찾았니==False:
            print('할 일을 찾을 수 없습니다')