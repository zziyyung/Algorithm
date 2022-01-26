#우주선 발사 카운트다운

#함수
def countDown(num):
    if num == 0:
        print('발사!')
    else:
        print(num)
        countDown(num-1)

#전역


#메인
print(countDown(5))