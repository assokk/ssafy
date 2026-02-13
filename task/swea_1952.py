# month는 실제 월에서 -1
def dfs(month, fee):
    global answer

    if fee >= answer:
        return

    if month >= 12:  # 3달, 1년
        if answer > fee:
            answer = fee
        return

    # 일권
    dfs(month+1, fee + day_fee * days[month])

    # 월권
    dfs(month+1, fee + month_fee)

    # 3개월권
    dfs(month+3, fee + quarter_fee)


'''
1일 이용권 사는 사람 : 해당 달은 일일권만 사겠다는 뜻

'''

T = int(input())

for tc in range(1, T+1):
    day_fee, month_fee, quarter_fee, answer = map(int, input().split())
    days = list(map(int, input().split()))

    dfs(0, 0)


    print(f'#{tc} {answer}')