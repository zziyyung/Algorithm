# 상하좌우

# 연산횟수는 이동 횟수에 비례
# 이동횟수가 N번인 경우 시간 복잡도 O(N) ; 넉넉한 편
# 시뮬레이션 유형 : 일련의 명령에 따라서 개체를 차례대로 이동

N = int(input())
plans = input().split()  # 알아서 리스트 요소로 들어감

# (1,1)이 무조건 시작점이니까 1,1 값 주고 시작
x , y = 1 , 1

# 이동방향 설정
move_type = ['L','R','U','D']
dx = [0,0,-1,1]  # x 는 위,아래 방향
dy = [-1,1,0,0]  # y는 왼,오 방향

# 이동 계획 하나씩 확인
for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 초과할 경우 무시
            if (nx<1) or (ny<1) or (nx>N)  or (ny>N):
                continue

            x , y = nx, ny

print(x,y)

