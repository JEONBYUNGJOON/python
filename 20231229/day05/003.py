jumin='961011-1021023'
gender=jumin[7]

# 남자인지 여자인지
if gender =='1':
    print('남자')
else:
    print('여자')
# 둘중의 하나 if문을 한줄로 -> 삼항연산자
# 복잡한 조건 삼항연산자를 쓰지말자 - 스파게티 코드(읽기 어려운 코드)  /  # 스파게티 코드, 외계인 코드
print("남자" if gender=="1" else"여자") #식 / type - str(실행)

# gender 가 1또는3또는5면 남자, 아니면여자
"남자" if gender=='1' or gender=='3' or gender=='5' else"여자"
"남자" if gender in ('1','3','5') else '여자'

# 주민번호로 나이 출력하기
# 1. 올해의 년도
# 2. 태어난 년도
#    주민번호 앞 2자리를 슬라이싱한다 - > year
#    주민번호가 7번째가 '1' , '2' -> '19' + year
#    주민번호가 7번째가 '3' , '4' -> '20' + year
# 3. 올해의 년도 - int(태어난년도)
import datetime
this_year = datetime.datetime.now().year
year = jumin[0:2]
if jumin[7] in ('1','2'):
    year = int('19' + year)
elif jumin[7] in ('3','4'):
    year = int('20' + year)
print(f'{this_year-year}세')
