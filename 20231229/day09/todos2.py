# 할 게임 : 게임번호, 게임종류, 게임 종료 여부

todos = []

todos.append({'tno':1, 'title': '리그오브레전드', 'finish': False})
todos.append({'tno':2, 'title': '배틀그라운드', 'finish': False})
todos.append({'tno':3, 'title': '스타그래프트', 'finish': False})
todos.append({'tno':4, 'title': '메이플스토리', 'finish': False})

while True:
    print('##### 할 게임 관리 ######')
    print('1:게임 목록, 2:게임 추가, 3:게임 변경, 4: 삭제, 999: 종료' )
    select = input('메뉴 선택')
    if select=='1':
        
