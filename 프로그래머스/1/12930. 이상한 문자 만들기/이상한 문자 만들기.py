# 공백을 기준으로 각 단어 별 인덱스 부여
def solution(s):
    answer = '' 
    # 1. 공백을 기준으로 분할한 단어를 리스트에 넣는다 
    words = s.split(' ')
    print(words)

    # 2. 단어들을 한번씩 순회하면서 짝수 = 대문자, 홀수= 소문자 적용
    for word in words:
        for w in range(len(word)):
            if w%2 == 0:
                answer += word[w].upper()
            else:
                answer += word[w].lower()
        # 3. 단어 1개 순회가 끝났을 때는 빈칸을 더해준다 
        answer += ' '
    return answer[:-1]
