# 1이 될 때까지

N,K = map(int,input().split())

# N이 K의 배수라면 1이 나올 때 까지 나누면 되지만
# 아니라면 N을 -1씩 해서 K의 배수가 될 때까지 만들어준다

cnt = 0

while N != 1 :
    if N % K == 0:
        N = N//K
        cnt += 1

    else:
        N = N - 1
        cnt += 1

print(cnt)