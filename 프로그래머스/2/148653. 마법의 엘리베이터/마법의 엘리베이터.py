def solution(storey):
    answer = 0

    while storey:
        point = storey % 10
        # 6~9
        if point > 5:
            answer += (10-point)
            storey += 10
        # 0~4
        elif point < 5:
            answer += point
        # 5
        else:
            if (storey//10) % 10 > 4:
                storey += 10
            answer += point
        storey //= 10

    return answer