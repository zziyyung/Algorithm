from itertools import permutations
def solution(numbers):
    # 숫자 조합을 담을 set
    prime_set = set()

    # 1. 모든 숫자 조합을 만든다
    for i in range(len(numbers)):
        numbers_permutations = permutations(list(numbers), i+1)
        numbers_perm_list = map(int,map(''.join, numbers_permutations))
        prime_set |= set(numbers_perm_list)
        # print(prime_set)

    # 2. 소수가 아닌 수를 제외한다
    # 2-1. 0과 1 제외
    prime_set -= set(range(0,2))
    # 2-2. 가장 큰 수의 제곱근까지 확인
    limit = int(max(prime_set) ** 0.5) + 1

    for i in range(2,limit):
        prime_set -= set(range(i*2, max(prime_set)+1, i))

    return len(prime_set)