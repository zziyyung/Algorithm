# 백중 11047번 동전0

N,K = map(int,input().split())


coins = list()

for i in range(N):
    coins.append(int(input()))

coins.reverse()

cnt = 0

for coin in coins:
    cnt += (K//coin)
    K %= coin

print(cnt)