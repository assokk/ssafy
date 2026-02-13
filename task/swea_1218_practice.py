for tc in range(1, 11):
    N = int(input())
    txt = input()

    top = -1
    stack = [0] * N
    ans = 1

    for x in txt:
        if x in '[{(<':
            # top을 1 증가시켜서 해당 위치에 x를 저장
            top += 1
            stack[top] = x
        elif x in '>)}]':
            # stack이 비어있는지 확인
            if top == -1:
                ans = 0
                break
            else:
                # 가장 마지막에 열린 괄호가 가장 먼저 닫혀야 하므로
                # x와 top에 있는 열린 괄호가 짝이 맞는지 비교
                if stack[top] == '<' and x == '>':
                    top -= 1
                    continue
                elif stack[top] == '(' and x == ')':
                    top -= 1
                    continue
                elif stack[top] == '{' and x == '}':
                    top -= 1
                    continue
                elif stack[top] == '[' and x == ']':
                    top -= 1
                    continue
                else:
                    ans = 0
                    break
    # 문자열을 다 돌고 난 뒤 스택이 비어있지 않다면
    # 여는 괄호가 남아있다, 즉 짝이 맞지 않는 것이므로 오류
    if top != -1:
        ans = 0

    print(f'#{tc} {ans}')
