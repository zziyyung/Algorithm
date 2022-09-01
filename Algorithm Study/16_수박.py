# 프로그래머스_수박수박수박수박수박수?

# 짝수이면 수 , 홀수이면 박

n = int(input())
List = []

for i in range(n):
    if i ==0 or i % 2 == 0 :
        List.append("수")
    else:
        List.append("박")

for j in List:
    print(j,end='')
