T = int(input())

for tc in range(1, T+1):
    day_cost, month_cost, quarter_cost, answer = map(int, input().split())  # 연간권을 answer로 받으면 연간권을 구매하는 경우를 고려할 필요가 없어짐
    plans = list(map(int, input().split()))

    dp = [0] * 12
    dp[0] = min(month_cost, day_cost*plans[0])  # 해당 월까지 사용하는 값 중 더 작은 값

    for current in range(1, 12):
        dp[current] = dp[current - 1] + min(month_cost, day_cost * plans[current])
        
        # 3개월권을 사는 것은 2번달(3월)부터 유의미함
        if current - 2 >= 0:    # 따라서 2번달 이상이면
            # 원래 이전 금액도 합쳐주어야 하는데, 현재 2번달이고 3개월권을 구매한다면 인덱싱 문제가 발생
            # 근데 파이썬에서는 인덱싱이 dp[-1] = dp[11] = 0 으로 나오기 때문에 괜찮다
            dp[current] = min(dp[current], dp[current-3] + quarter_cost)

    answer = min(answer, dp[11])

    print(f'#{tc} {answer}')