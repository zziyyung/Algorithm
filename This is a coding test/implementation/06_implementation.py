# 문자열 재정렬

S = input()
alphaList = []
sum = 0

for i in range(len(S)):
    if S[i].isnumeric():
        sum += int(S[i])
    else:
        alphaList.append(S[i])

alphaList.sort()

if sum != 0:  # 숫자가 하나라도 존재한다면
    alphaList.append(str(sum))

print(''.join(alphaList))