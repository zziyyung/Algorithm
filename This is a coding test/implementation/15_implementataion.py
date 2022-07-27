# 백준 14719 : 빗물

# 높이와 밑길이 입력받기
h,w = map(int,input().split())

# 블록 값 받기
data = list(map(int,input().split()))

# 물이 쌓이기 위해서는 기준점을 기준으로 양쪽 블럭이 기준점 높이보다 높아야함
# 그리고 고이는 물의 높이는 둘 중 더 작은 높이에서 기준점의 높이를 뺀 만큼  고인다
water = 0
for i in range(1,w-1):
    left = max(data[:i])
    right = max(data[i+1:])

    val = min(left,right)
    if val > data[i]:
        water += val-data[i]

print(water)