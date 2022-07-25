# 기둥과 보 설치

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 기둥 , 보 좌표 기준 오른쪽/위 설치
# 삭제할 경우에도 위의 두 조건 만족해야함 ( 만족 못할 경우 무시 )


# 출력시
# [x,y,a] x 기준으로 오름차 , y 기준으로 오름차

# 2가지 조건 확인
def possible(answer):
    for x,y,stuff in answer:
        #설치된 것이 기둥이라면
        if stuff == 0 :
            # 바닥 위  / 보의 한쪽 끝부분 위 / 다른 기둥 위  == 정상
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            # 아니라면
            return False
        # 설치된 것이 보라면
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위 / 양쪽 끝부분이 다른 보와 동시에 연결
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

# 실제 시뮬
def solution(n, build_frame):
    answer = []
    # 작업 개수는 최대 1,000개
    for frame in build_frame:
        x,y,stuff,operate = frame
        # 삭제하는 경우
        if operate == 0:
            # 일단 삭제해보고
            answer.remove([x,y,stuff])
            # 가능한 구조물인지 확인
            if not possible(answer):
                # 가능하지 않다면 다시 설치
                answer.append([x,y,stuff])
        # 설치하는 경우
        if operate == 1:
            answer.append([x,y,stuff])
            # 가능한 구조물인지 확인
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)