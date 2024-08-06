# 왕실의 나이트

data = input()   # 문자열에서 바로 인덱싱 가능
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1  # a:1 , b;2 , c:3 , ...

# 나이트가 이동할 수 있는 방향 정리
steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

# steps를 한 번씩 보면서 각 위치로 이동이 가능한지 확인
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_row <= 8 and next_column >=1 and next_column <=8:
        result += 1

print(result)
