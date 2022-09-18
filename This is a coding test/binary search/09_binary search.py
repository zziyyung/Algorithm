# 가사 검색

from bisect import bisect_left, bisect_right

def count_by_range(array, left_val, right_val):
    left_idx = bisect_left(array, left_val)
    right_idx = bisect_right(array, right_val)
    return right_idx - left_idx

def solution(words, queries):
    answer = [0] * len(queries)
    asc_words = [[] for _ in range(100001)]
    desc_words = [[] for _ in range(100001)]
    # 단어 길이를 인덱스로하는 2차원 리스트에 단어 길이별로 담기
    for word in words:
        asc_words[len(word)].append(word)
        desc_words[len(word)].append(word[::-1])

    # 단어 길이별로 단어들 정렬
    for i in range(100001):
        asc_words[i].sort()
        desc_words[i].sort()

    # 쿼리하나씩 받아서 처리
    for i in range(len(queries)):
        q = queries[i]
        if q[0] != '?':
            answer[i] = count_by_range(asc_words[len(q)], q.replace('?', 'a'),
                                       q.replace('?', 'z'))
        else:
            q = q[::-1]
            answer[i] = count_by_range(desc_words[len(q)], q.replace('?', 'a'),
                                       q.replace('?', 'z'))

    return answer