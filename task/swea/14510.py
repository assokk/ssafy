T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_length = max(arr)
    length_gap = []

    need1 = 0
    need2 = 0
    answer = 0

    for i in arr:
        length_gap.append(max_length-i)

    for gap in length_gap:
        need1 += gap % 2
        need2 += gap // 2

    # 이미 같은 높이라면
    if need1 == 0 and need2 == 0:
        result = 0
    else:
        if need2 > need1:
            while need2 - need1 > 1:
                need2 -= 1
                need1 += 2

        if need2 > need1:
            answer = need2 * 2
        elif need2 == need1:
            answer = need2 * 2
        else:
            answer = need1 * 2 - 1 

    print(f'#{tc} {answer}')
    