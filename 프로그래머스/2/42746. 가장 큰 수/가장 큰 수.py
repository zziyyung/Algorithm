def solution(numbers):
    answer = ''

    # 1.리스트의 각 숫자를 문자열로 치환 후 내림차순 정렬한다.
    numbers = list(map(str, numbers))
    # 1-1. 내림차순 정렬시 3, 30과 같은 수를 처리하기 위해 각 자리의 숫자를 3번 곱한 수로 비교하여 정렬한다.
    numbers.sort(key=lambda x: x*3 ,reverse=True)

    # 2. 정렬된 순서대로 값을 이어 붙인다.
    for i in numbers:
        answer += i

    # 3. 0이 들어온 경우 00으로 나오는 case를 예외처리하기 위해 int로 형변환 후 다시 str으로 변환해준다.
    return str(int(answer))