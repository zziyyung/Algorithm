#팩토리얼 구하기

#함수
def mulNumber(num):
    if num <=1:
        return 1
    else:
        return num*mulNumber(num-1)

#전역


#메인
print(mulNumber(5))