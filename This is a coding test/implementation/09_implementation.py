# 뱀

n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수
data = [[0]*(n+1) for _ in range(n+1)] # 맵 정보 ( 2차원 리스트 생성 ) , 범위 n+1 해줘야함

# 맵 정보 ( 사과 있는 곳을 '1'로 표시 )
for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
info = [] # 방향 회전 정보
l = int(input()) # 몇 번 방향 전환 했는지
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))  # 튜플 형태로 넣기 ?

# 처음에는 오른쪽(동쪽)을 보고 있으므로 ( 동, 남, 서, 북 )
dx = [0,1,0,-1] # 남 , 북
dy = [1,0,-1,0] # 동 , 서

#  direction으로 위의 dx,dy에서 동,남,서,북 위치를 더할 것임 ( 그래서 4로 나눈 나머지 )
def turn(direction,c):
    if c=='L':    # 왼쪽(반시계)으로 꺾을 경우 (-1)
        direction = (direction-1) % 4
    else:         # 오른쪽(시계)으로 꺾을 경우 (+1)
        direction = (direction+1) % 4
    return direction

def simulate():
    x,y = 1,1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 '2'로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 게임이 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보 (info 리스트에서 카운트하기 위함)
    q = [(x,y)] # 뱀이 차지하고 있는 위치 정보 ( 꼬리가 앞쪽 )
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<= nx and nx <=n and 1 <=ny and  ny <=n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)  # 원래 있던 정보 빼기 ( 사과를 안 먹어서 몸이 안 늘어났으니까 )
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        # 벽이나 뱀의 몸과 부딪혔다면
        else:
            time += 1
            break
        x,y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index <1 and time == info[index][0]: # 회전할 시간인 경우 회전 ####
            direction = turn(direction,info[index][1])
            index += 1
    return time
print(simulate())
