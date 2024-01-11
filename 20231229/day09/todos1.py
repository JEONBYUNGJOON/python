todos=[]
# 할일 : 할일번호, 할일, 완료
todos.append({'tno':1, 'title':'자바공부', 'finish':False})
todos.append({'tno':2, 'title':'스프링 공부', 'finish':False})
todos.append({'tno':3, 'title':'파이썬 공부', 'finish':False})
tno = 4

def print_todos():
    for todo in todos:
        print(todo)
        
def add_todo():
    # 함수 안에서 함수 밖에 있는 변수를 변경하려면 global 변수이름
    global tno
    title = input('할입 입력:')
    todos.append({'tno':tno, 'title':title, 'finish':False})
    tno=tno+1

def toggle_finish():
    pass

def delete_todo():
    pass

while True:
    print('### 할일 관리 ###')
    print('1:목록, 2:추가, 3:변경, 4:삭제, 999:종료')
    
    select = input('메뉴 선택:')
    if select=='1':
        print_todos()            # 호출
    elif select=='2':
        add_todo()
    elif select=='3':
        toggle_finish()
    elif select=='4':
        delete_todo()
    elif select=='999':
        print('이용해주셔서 감사합니다')
        break