def solution(phone_book):
    # 1. 정렬, O(n log n)
    phone_book.sort()
    # 2. 앞의 수가 뒤의 수로 시작하는 경우는 없기 때문에, 뒤의 수가 앞의 수로 시작하는지만 확인, O(n * m)  
    for a,b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True