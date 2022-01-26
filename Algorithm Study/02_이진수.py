#혜인님
T = int(input())     # 테스트 개수
for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end=' ')
    print()

#정윤님
t = int(input())
for _ in range(t):
    n = int(input())
    i = 0
    while n > 0:
        if n % 2 == 1:
            print(i, end=' ')
        n //= 2
        i += 1
    print()
