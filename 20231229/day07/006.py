import e005
from e005 import hello, print_python

# e005에 파이썬이라고 출력하는 함수를 정의하고 006.py에서 호출하시오
e005.print_python()
print_python()

def message():
    print("A")
    print("B")

# 함수는 동시에 실행되지 않는다(한번에 하나씩 실행) 
# 병렬 프로그래밍 : 함수를 동시에 실행하는 것
message()
print("C")
message()