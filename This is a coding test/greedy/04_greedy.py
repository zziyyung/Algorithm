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


N,K = map(int,input().split())

cnt = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (N//K) * K
    cnt += (N - target)
    N = target

    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break

    cnt += 1
    N //= K

# 마지막으로 남은 수에 대하여 1씩 빼기
cnt += (N-1)
print(cnt)