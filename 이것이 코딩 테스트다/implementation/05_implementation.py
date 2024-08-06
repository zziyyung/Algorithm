# 럭키 스트레이트

N = input()
length = len(N)
sum = 0

for i in range(length//2):
    sum += int(N[i])

for j in range(length//2,length):
    sum -= int(N[j])

if sum == 0:
    print('LUCKY')
else:
    print('READY')