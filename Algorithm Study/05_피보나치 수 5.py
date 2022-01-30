#백준 10870번

#함수 선언부
def Fibonacci(n):
    sum=0

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2, n + 1):
            sum= Fibonacci(i-1)+ Fibonacci(i-2)
        return sum

#메인코드
n=int(input())
if n<0 or n>20 :
    print("0에서 20 사이 숫자를 입력하세요")
else:
    print(Fibonacci(n))





# # #혜인님
# # n 입력 받음 (20보다 작거나 같은 자연수 또는 0)
# while True:
#     n = int(input())
#     if 0 <= n <= 20:
#         break
#
#
# # 피보나치 수 구하기
# def Fibonacci(n):
#     sum = 0
#
#     if (n == 0):  # 0번째 피보나치 수
#         return 0
#     elif (n == 1):  # 1번째 피보나치 수
#         return 1
#     else:  # n이 2이상인 피보나치 수
#         for i in range(2, n + 1):
#             sum = Fibonacci(i - 1) + Fibonacci(i - 2)
#         return sum
#
#
# # n번째 피보나치 수 출력
# print(Fibonacci(n))


# #정윤님
# try:
#     n = int(input())
#     if not 0 <= n <= 20:
#         raise Exception("범위를 벗어났습니다.")
#     fibo = [0, 1]
#     for i in range(n):
#         fibo.append(fibo[i] + fibo[i + 1])
#     print(fibo[n])
# except Exception as e:
#     print(e)

