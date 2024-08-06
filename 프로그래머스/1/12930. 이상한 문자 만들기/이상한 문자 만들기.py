def solution(s):
    answer = '' 
    words = s.split(' ')
    print(words)

    for word in words:
        for w in range(len(word)):
            if w%2 == 0:
                answer += word[w].upper()
            else:
                answer += word[w].lower()
        answer += ' '
    return answer[:-1]