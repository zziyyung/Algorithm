# 게임 개발

# nxm 좌표평면
n,m = map(int,input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 (리스트 컴프리헨션 사용)
d_map = [[0]*m for _ in range(n)]
#print(d_map)

# 현재 캐릭터의 x,y좌표와 방향 d 입력 받기
x,y,d = map(int,input().split())

# 현재 좌표 방문처리
d_map[x][y] = 1  # 방문했을 경우 1로 표기

# 전체 맵 정보 입력 받기
array = []
for i in range(n):
    array.append(list(map(int,input().split())))  # 한 줄씩을 하나의 리스트에 담아서 array에 넣기

# 북, 동, 남 , 서 방향 설정
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global d  # 방향 변수인 d가 turn_left함수의 바깥에서 선언된 전역변수라 사용하기 위해서 global 선언
    d -= 1    # 왼쪽으로 돌기 위해서 -1 해줌 ( 북 : 0, 동 :1 , 남:2 , 서:3 )
    if d == -1:  # '북'에서 -1을 한 '-1'값이 되었을 때는 다시 '서'로 입력
        d=3

# 시뮬레이션 시작
count = 1  # 현재 서 있는 위치 방문 카운트 하기 ! (1부터 시작하는 이유)
turn_time = 0  # 회전 개수

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # 회전 후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d_map[nx][ny] == 0 and array[nx][ny] == 0:
        d_map[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전 후에 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤가 바다로 막혀있다면
        else :
            break

        turn_time = 0

print(count)