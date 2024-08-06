def solution(s):
    s = s.lower()

    p_cnt = s.count("p")
    y_cnt = s.count("y")

    if p_cnt == y_cnt:
        return True
    return False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

