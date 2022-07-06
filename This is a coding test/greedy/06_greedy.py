# 곱하기 혹은 더하기

# 0과 1을 연산할 때만 +를 사용하고 나머지는 다 * 로 계산

S = input()

sum = int(S[0])

for i in range(1,len(S)):

    num = int(S[i])  # sum에 0번째 값을 먼저 대입했기 떄문에 , 1번째부터 시작

    if sum <= 1 or num <= 1:
        sum += num
    else:
        sum *= num

print(sum)