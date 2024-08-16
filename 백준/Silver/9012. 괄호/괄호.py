T = int(input())

for i in range(T):
    ps_string = input()
    ps_sum = 0
    for j in ps_string:
        if j == '(':
            ps_sum += 1
        else :
            ps_sum -= 1
            if ps_sum < 0:
                print("NO")
                break
    if ps_sum == 0:
        print("YES")
    elif ps_sum > 0:
        print("NO")