def solution(s,n):
    # 1. 문자열을 리스트로 치환 
    s = list(s)

    # 2. 문자열을 하나씩 순회하면서 대문자일 경우, 소문자일 경우 처리해준다다
    for i in range(len(s)):
        if s[i].isupper():
            # 3. ((해당 문자열 - 시작문자) + n )% 26 = 항상 26 범위 이내로 몇 칸 이동하는지 도출 가능
            # 4. 시작 문자열에 이동 수를 더한 뒤 문자로 변환해준다다
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return ''.join(s)