'''
(6+5*(2-8)/2)
6528-*2/+
'''

# 후위 표기법 변환
stack = [0] * 10
top = -1

icp = {'(':3, '*':2, '/':2, '+':1, '-':1}  # 스택 밖에서의 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}  # 스택 안에서의 우선순위

infix = '6+5*(2-8)/2'  # 중위식 문자열
postfix = ''

for token in infix:
    if token not in '(*/+-)':   # 피연산자면 후위식에 추가
        postfix += token
    elif token == ')':          # 닫는 괄호면 여는 괄호를 만날 때까지 pop
        while top > -1 and stack[top] != '(':
            top -= 1
            postfix += stack[top + 1]
        # while stack and stack[-1] != '(':   # .append() / .pop()
        #     postfix += stack.pop()
        if top != -1:
            top -= 1    # '(' 제거
    else:   # '(*/+-'인 경우
        if top == -1 or isp[stack[top]] < icp[token]:
            top += 1
            stack[top] = token
        elif isp[stack[top]] >= icp[token]:
            while top > -1 and isp[stack[top]] >= icp[token]:
                top -= 1
                postfix += stack[top + 1]
            top += 1            # 스택의 마지막 연산자보다 
            stack[top] = token  # 우선순위가 높아졌으므로 push

    print(postfix, stack, top)

while top > -1:
    top -= 1
    postfix += stack[top + 1]

print(postfix)


# 후위 표기법 연산
stack = []
for token in postfix:
    if token not in '*/+-':         # 피연산자면 push
        stack.append(int(token))    # token은 문자열이니까
    else:                   # 연산자면
        op2 = stack.pop()   # 오른쪽 피연산자
        op1 = stack.pop()   # 왼쪽 피연산자
        result = 0
        if token == '*':
            # stack.append(op1 * op2)
            result = op1 * op2
        elif token == '/':
            result = op1 / op2
        elif token == '+':
            result = op1 + op2
        elif token == '-':
            result = op1 - op2
        stack.append(result)    # 연산결과 push
answer = stack.pop()
print(f'{answer:.0f}')
print(f'{9.46:.1f}')
print(f'{int(9.5)}')
