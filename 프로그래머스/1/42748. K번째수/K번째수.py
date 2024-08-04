def solution(array, commands):
    answer = []

    # 1. commands를 돌며 i부터 j번까지 자른다
    for i in range(len(commands)):
        start, end, k = commands[i]

        # 2. 정렬한다
        sorted_arr = sorted(array[start-1:end])

        # 3. k번째 수를 리스트에 담는다
        answer.append(sorted_arr[k-1])

    return answer