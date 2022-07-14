# 문자열 압축

def solution(s):
    answer = len(s)

    # 1개 단위부터 압축 단위를 늘려가면서 확인
    for step in range(1,len(s)//2+1): # len(s)//2 한 것까지만 확인하면 됨
        compressed = ""  # 압축한 문자열
        prev = s[0:step]  # 이전 문자 or 문자열
        count = 1  # 압축 횟수

        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for i in range(step,len(s),step):
            # 이전 상태와 같다면 압축횟수 +1 하기
            if prev == s[i:i+step]:
                count += 1
            # 이전 상태와 같지 않아 더 이상 압축 못 하는 경우
            else:
                compressed += str(count)+prev if count >=2 else prev  # str(count)
                prev = s[i:i+step]
                count = 1
        # 남아있는 문자열 처리
        compressed += str(count)+prev if count>=2 else prev
        answer = min(answer,len(compressed))
    return answer