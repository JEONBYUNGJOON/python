# 나이를 입력받아 성년여부를 리턴하는 함수

# 20        성년입니다,  15           미성년입니다

def is_adult(nai:int):
    if nai>=18:
        return True
    else:
        return False
    
nai=25
if is_adult()==True:
    print("당신은 출입가능합니다")
