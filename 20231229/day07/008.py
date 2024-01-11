# 정수 2개를 인자로 받아 덧셈 후 출력하는 함수를 정의하고 호출
def hap(a:int|float,b:int|float):
    print(a+b)

def hap2(a:int|float, b:int|float):
    # return 결과 -> 함수를 종료하고 결과로 바꿔라
    return a+b

print(hap2(3,4))

result = hap2(3,4)