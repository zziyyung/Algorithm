# 무지의 먹방 라이브
food_times = [3,1,2]

# k 연산 후 재정렬 시 필요
from operator import itemgetter

def solution(food_times, k):
    # 1. 음식 먹는데 소요되는 시간순으로 리스트 정렬하기

    # food 리스트를 생성 ( 음식 먹는데 소요되는 시간 순서로 정렬하기 위한 리스트 )
    foods = []

    # food 리스트에 값 넣기 ( 음식 먹는데 소요되는 시간 , 음식 번호 ) -> 튜플형태로 넣기
    for i in range(len(food_times)):
        foods.append((food_times[i],i+1))

    # 음식 먹는데 소요되는 시간이 작은 순서대로 정렬
    # 튜플은 앞에 있는 값을 기준으로 정렬함
    foods.sort()
    #print(food)


    # 2. K에서 (음식먹는데 소요되는 시간 * 남은 음식 개수) 빼기 ( 단 , K보다 커지지 않을 때까지)
    # 연산에 필요한 음식 개수
    n = len(food_times)

    # 이전 시간
    pretime = 0

    for i, food in enumerate(foods):
        # 음식 먹는데 필요한 시간 - 전 시간  ( 그리드 그림에서 세로축이 됨 = 높이 )
        # food[0] = 음식 먹는데 필요한 시간
        diff = food[0] - pretime

        # 음식먹는데 필요한 시간 * 남은 음식 수
        if diff != 0 :
            spend = diff * n

            # k에서 빼주기
            if spend <= k:
                k -= spend

                # 이전 시간 바꿔주기
                pretime = food[0]

    # 3. k에서 빼는 경우가 -가 된다면 멈추고 , k 나누기 남은 음식 후 정렬해서 답을 구한다
            # k에서 못 빼는 경우
            else:
                k %= n
                # 재정렬 , 음식 번호로 정렬
                # foods[i:] : foods 배열에서 남은 i번째부터 끝까지
                # foods[1] (1번 인덱스 사용하기 위해서) operator 모듈에서 itemgetter 사용 , itemgetter(1) -> 1번부터 정렬
                sublist = sorted(foods[i:],key=itemgetter(1))
                # 나머지 음식에서 그 다음 먹어야하는 번호를 써줘야하니까 인덱스 1 붙임 [k][1]
                return sublist[k][1]

        # 한 번 연산하고 난 후에 음식 개수 줄여야하니까 -1씩 해준다
        n -= 1

    # for문이 돌아도 return이 안 된다는 건 연산이 안 되는거니까 ( 다 먹었으니까 ) -1 반환
    return -1

#solution(food_times,5)