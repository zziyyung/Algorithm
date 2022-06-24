# 2504번
# 스택의 응용 : 괄호의 값
# 알고리즘 분류 : 구현 , 자료 구조 , 스택 , 재귀
# 스택 : 선입후출 (입구와 출구가 동일한 형태:박스쌓기) ,list (append,pop) 로 구현
# 큐 : 선입선출 (입구와 출구가 모두 뚫려있는 터널) . deque() append, popleft

# ( ) [ ]
# 올바른 괄호열 : () []

# 첫째 줄 : 괄호열을 나타내는 문자열 ( 1이상 30 이하)
# import sys
# Input = sys.stdin.readline()
# if len(Input) < 1 or len(Input) >31:
#     print ('다시 입력')


# 1. 올바른 괄호열과 올바르지 않은 괄호열 구분
## 올바른 괄호열의 조건 '(' ')' '[' ']'    --> 파이썬 스트링 예제 문제 중 이메일 적용 @ , .

# 사이에 값이 있어도 되고 없어도 되나 '(' 있으면 ')'로 마무리

# 첫 시작은 (, [ 로 / 끝은 ),]로 !
# 순서가 바뀌면 안된다
# ( ( 안 되고 ) ) 안 되고 ()만 됨 = 개수가 맞아야함 = ()() (( ))

# (), [] 가 오류 -> (, [ 둘 중 하나만 있어도 되는데


# 시작 문자 리스트 와 끝 문자 리스트를 따로 만들어서 그 안에서 확인 !
# start = [ '(' , '[' ]
# end = [ ')' , ']' ]
# start_lo = Input[0]
# last_lo = Input[-1]

# if (Input.find(')') == 0) or (Input.find(']') == 0) or \
#     (Input.find('(') == -1) or (Input.find('[') == -1) or \
#     (Input.find('(') > Input.find(')')) or (Input.find('[') > Input.find(']')) or \
#     (Input.count('(') != Input.count(')')) or (Input.count('[') != Input.count(']')) :
#     print('0')
# else:
#     print('일단 오케이')



# 2. 올바른 괄호열에 각각 값 부여
# 재귀함수 :  (), [] 안에 x값이 있으면  안에 값이 없을 때까지 다시 함수로 돌아가
def f(x):
    pass


# 3. 올바른 괄호열 연산법 설정 ( 올바르지 않은 괄호열은 0 )



# 참고
s = input()
stack = []
tmp = 1
res = 0

# for c in s를 하면 안 되고 길이로 돌아야 함
for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])

    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if s[i - 1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()  # pop도 까먹지 말고 꼭

    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
        # 단, 이 경우는 오류는 아님
        if s[i - 1] == '[':
            res += tmp
        tmp //= 3
        stack.pop()  # pop 까먹지 말기

if stack:
    res = 0
print(res)