# 1년은 몇초인지 출력
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = 60
print(DAYS_PER_YEAR*HOURS_PER_DAY*MINUTES_PER_HOUR*SECONDS_PER_HOUR)

# 45분간 일하고 10분씩휴식. 전체 근무시간 480분이면
# 휴식 시간의 합계는 얼마인가?
times = 480//55
휴식시간합계  =times*10
print(휴식시간합계)

# 숫자를 입력받아 1의 자리까지 버리고 출력
# 예) 3512->3510, 359->350

# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
# 예) 17->14, 21->21
# 1-6     0       7*0  
# 7-13    //7       7*1
# 14-20   14      7*2

# 자연수를 입력받아 그 숫자보다 작은 최대의 7의 배수
# 예) 17-> 14, 21->14
# 1-7       0       7*0
# 8-14      //7     7*1
# 15-21     14      7*2
num=14
mok=(num-1)//7
print(mok*7)

# 예) 17-> 14, 21->14
# 1-7       0       7*0
# 8-14      //7     7*1
# 15-21     14      7*2
num=14
mok = num//7
if num%7==0:
    mok=mok-1
print(mok*7)