# 백준 2615 : 오목

# 바둑판 범위
n = 19

# 오목이 될 수 있는 경우의 수는 ' 아래 , 우하향 , 오른쪽 , 우상향 ' 4가지
dx = [1,1,0,-1] # x축 (가로선)을 기준으로 이동했을 때의 좌표 변화
dy = [0,1,1,1]  # y축 (세로선)을 기준으로 이동했을 때의 좌표 변화

# 바둑판 정보 리스트에 담기
data = [ list(map(int,input().split())) for _ in range(19)]

# 오목 확인하는 함수 omok()
def omok():
    # 초기 승리는 0 으로 설정
    win = 0
    # 오목 배열판을 2차원리스트로 입력받아 , 이중for문으로 오목리스트를 하나하나 확인
    for x in range(n):
        for y in range(n):
            # 빈 공간 (0)이라면 굳이 아래의 연산을 할 필요가 없음
            if data[x][y] != 0:
                # 첫 바둑돌을 세어야하니까 1로 시작
                cnt = 1
                # 아래,우하향,오른쪽,우상향 총 4번을 하나씩 같은색 바둑돌 있는지 확인
                for i in range(4):
                    # 이동한 좌표
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 바둑돌이 현재 바둑판 위에 있고 , 이전 좌표의 값과 이동한 좌표의 값이 같다면 cnt+1
                    while 0 <= nx < 19 and 0 <= ny < 19 and data[x][y] == data[nx][ny]:
                        cnt += 1

                        # 이동한 그 좌표상의 위치에서 또 그 다음을 살펴봐야하니까
                        nx += dx[i]
                        ny += dy[i]

                    # 육목판정
                    if cnt == 5:
                        # 이미 같은색의 바둑돌의 개수가 5개가 되었는데, 위와 같은 조건에서 또 같은 색이 나왔다면?
                        if 0 <= nx < 19 and 0 <= ny < 19 and data[x][y] == data[nx][ny]:
                            break
                        # 첫기준의 전 좌표도 살펴보기
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and data[x][y] == data[x-dx[i]][y-dy[i]] :
                            break

                        # 육목에 해당이 안 되는 오목이라면 처음의 색깔이 승리
                        else:
                            win = data[x][y]

                        return win,x,y
    return win,0,0

win,x,y = omok()

if win == 0:
    print(win)
else:
    print(win)
    print(x+1,y+1)