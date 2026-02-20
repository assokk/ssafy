for tc in range(1, 11):
    N = int(input())
    fx = input()

    stack = [0] * 101
    top = -1

    susik = ''
    for x in fx:
        if x != '+':
            susik += x
        else:
            while top > -1:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x
    
    while top > -1:
        susik += stack[top]
        top -= 1


    for x in susik:
        if x != '+':
            top += 1
            stack[top] = int(x)
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            
            top += 1
            stack[top] = op1 + op2

    print(f'#{tc} {stack[top]}')