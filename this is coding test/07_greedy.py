# 문자열 뒤집기

S = input()

cnt0 = 0  # 1에서 0으로 바뀌는 횟수
cnt1 = 0  # 0에서 1로 바뀌는 횟수

# 첫 번째 값 처리
if S[0] == '1':  # 문자열이기 때문에 '' 사용
    cnt0 += 1
else:
    cnt1 += 1

# 두 번째 값부터 모든 값 확인하면서
for i in range(len(S)-1):  # 인덱스 범위 초과하지 않기 위해 -1
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0,cnt1))


# 다른 풀이

# S = input()

# count = 0

# for i in range(len(S)-1):
#     if S[i] != S[i+1]:
#         count += 1

# 0과 1 두 개의 패로 바꾸기 때문에 나누기 2
# 몫을 구해야 횟수가 나옴

# print((count + 1) // 2)