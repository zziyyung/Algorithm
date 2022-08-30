# 백준 10872 팩토리얼

def factorial(n):
    # n * n-1 * n-2 * n-3 ... * 1
    if n <= 1:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))