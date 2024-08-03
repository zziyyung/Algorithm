# 풀이1. sort & loop , O(n log n)
def min_line(lines):
    # 1. 시작값을 기준으로 정렬한다
    lines.sort(key=lambda x:x[0])

    # 2. 첫번째 선분 끝 값 = 현재 선분 끝 값으로 세팅
    current_end = lines[0][1]

    # 3. 선분 개수 1로 초기화
    count = 1

    for i in range(1,len(lines)):
        # 4-0. 시작값, 현재값 변수 세팅
        start, end = lines[i]

        # 4. 시작 값 > 현재 끝값 : 현재 끝값 = 시작값 , 선분 +1
        if start > current_end:
            count += 1
            current_end = end
        # 5. 시작 값 < 현재 끝값 : 끝 값, 현재 끝값 비교 후 더 큰 값으로 현재 끝값 업데이트
        else:
            current_end = max(current_end, end)

    return count

print(min_line([[1, 5], [3, 6], [7, 9]]))  # 출력: 2