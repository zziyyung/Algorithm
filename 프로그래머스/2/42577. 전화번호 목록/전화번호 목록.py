# 1. loop, O(n^2 * m), 시간 초과
# 모든 경우의 수를 탐색
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            # 반복문을 한 번 돌 때 "서로 체킹"
            # 두 문자열의 길이가 같은 최악의 경우 startswith은 O(m)
            if phone_book[i].startswith(phone_book[j]):
                return False
            elif phone_book[j].startswith(phone_book[i]):
                return False
    return True

# 2. sort&loop, O(n log n + n*m)
def solution(phone_book):
    # 1. 정렬, O(n log n)
    phone_book.sort()
    # 2. 앞의 수가 뒤의 수로 시작하는 경우는 없기 때문에, 뒤의 수가 앞의 수로 시작하는지만 확인, O(n * m)
    # for i in range(len(phone_book) - 1):
    #     if phone_book[i+1].startswith(phone_book[i]):
    #         return False

    # 번외. pythoninc하게 풀기
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True


# 3. 해시 O(n*m)
# key = 찾고자 하는 정보, value = 존재 유무 (1)
# 찾고자 하는 문자열의 문자를 하나씩 돌면서 해시맵에 해당 문자가 있는지 확인
# 단, 기존 번호와 동일한 경우는 제외
def solution(phone_book):
    # 1. 해시맵을 만든다, O(n)
    hashDict = {}
    for number in phone_book:
        hashDict[number] = 1


    # 2. 문자열의 문자열,문자열을 하나씩 비교하면서 해시맵에 있는지 확인한다, O(n*m)
    for number in phone_book:
        jubdoo = ''
        for i in number:
            jubdoo += i
            # 3. 있다면 False를 반환한다. 단, 비교 문자열 = 찾는 문자열 같을 경우는 제외, O(m)
            if jubdoo in hashDict and jubdoo != number:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))
