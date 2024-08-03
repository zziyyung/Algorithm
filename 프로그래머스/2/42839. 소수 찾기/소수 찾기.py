# 소수 = 2보다 큰 자연수 중 1과 자기 자신으로만 나눠지는 수
# 에라토스테네스의 체 = 여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘

# 1. loop & permutation
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


# 2. 재귀
# 내가 지금 하고 있는 행동은 무엇인지, 이 행동을 언제까지 해야하는지

# 1. 소수를 담을 set
prime_set = set()

def isPrime(number):
    # 6. 0과 1은 제외한다
    if number in (0,1):
        return False

    # 7. 에라토스테네스의 체
    limit = int(number ** 0.5 + 1)
    for i in range(2, limit):
        if number % i ==0:
            return False
    return True
def recursive(combination, others):
    # 5. 탈출 조건/ 비교 조건 : 지금까지 만들어진 조합을 소수인지 확인해준다
    # 5-1. combination에 숫자가 존재하는지 확인해주기
    if combination != '':
        if isPrime(int(combination)):
            prime_set.add(int(combination))

    # 4. 현재까지 만들어진 숫자에 남아있는 숫자를 하나씩 더해준다
    for i in range(len(others)):
        recursive(combination + others[i], others[:i]+others[i+1:])

def solution(numbers):
    # 2. 모든 조합을 만드는 recursive를 수행한다
    recursive("", numbers)

    # 3. prime_set의 길이를 반환한다
    return len(prime_set)

print(solution("17"))


# 번외) 에라토스테네스의 체
n = 1000
# 1. 처음에는 모든 수가 소수(True)라고 가정
array = [True for i in range(n+1)]

for i in range(2, int(n ** 0.5) + 1):
    if array[i]:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
