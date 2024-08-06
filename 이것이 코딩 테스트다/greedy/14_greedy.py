# 백준 1931번 회의실 배정

# 회의 겹치지 않게 회의실 사용할 수 있는 회의의 최대 개수 구하기

# 회의시간이 짧은 애들로 구성  (뒤 - 앞 )
# 뒤에 숫자랑 앞에숫자가 안 겹치게

meeting = int(input())

meeting_time = list()
for i in range(meeting):
    meeting_time.append(tuple(map(int,input().split())))

# 1 4
# 5 7
# 8 11
# 12 14

# 뒤에 값이랑 그 다음 앞에값을 비교해서 크다면 ..
# 뒤- 앞 차가 작은 것을 선택
# 위에 처럼 풀지 말고 정렬 사용하자 ! https://suri78.tistory.com/26

# 정렬 이용
#  1. 끝나는 시간의 오름차순 2. 시작하는 시간의 오름차순
# 근데 왜 x[1], x[0] ?  == 찾아보기
meeting_time.sort(key= lambda x: (x[1],x[0]))


cnt = 1

rear = meeting_time[0][1]

for j in range(1, meeting):
    if meeting_time[j][0] >= rear:
        cnt += 1
        # 두개다? 두개 중에 어떤거?
        # 막혔다
        # 정렬로 문제 풀 수 있음 ! 여기까지는 맞다 !!

        rear = meeting_time[j][1]

print(cnt)
