def solution(brown, yellow):
    answer = []

    # 1. x*y = yellow
    x = 0
    y = 0

    for i in range(1,yellow+1):
        if yellow % i == 0:
            x = i
            y = yellow // i
        # 2. (x+2) * (y+2) - (x*y) = brown
        # 2-1. 2x + 2y + 4 = brown
        if 2*x + 2*y +4 == brown:
            answer.append(x+2)
            answer.append(y+2)
            break
    answer.sort(reverse=True)

    return answer