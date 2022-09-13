# 정렬된 배열에서 특정 수의 개수 구하기

N, x = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = len(data) - 1
total = 0
while start <= end:
    mid = (start + end) // 2
    if x == data[mid]:
        for i in range(mid, -1, -1):
            if data[i] == x:
                total += 1
            else:
                break
        for j in range(mid + 1, len(data)):
            if data[j] == x:
                total += 1
            else:
                break
        break
    elif x >= data[mid]:
        start = mid + 1
    else:
        end = mid - 1

if total == 0:
    print(-1)
else:
    print(total)