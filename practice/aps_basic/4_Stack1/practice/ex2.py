
txt = input()
# 스택 생성
top = -1
stack = [0] * 100  # 입력최대 길이'
ans = 'OK'
for x in txt:
    if x == '(':
        top += 1
        stack[top] = '('
    elif x == ')':
    # elif x == ')}]':
        if top == -1:  # 여는 괄호가 없으면 오류
            ans = 'ERROR'
            # break
        else:          # 여는 괄호가 있으면 pop
            top -= 1
            # 괄호가 여러종류면 이 부분에서 비교
            # if stack[top+1] == '(' and x == ')':
            #     continue
            # elif stack[top+1] == '{' and x == '}':
            #     ...

if top != -1:
    ans = 'ERROR'
print(ans)