def calc_cost(K):
    return K*K+(K-1)*(K-1)

def search_K(K, cost):
    max_home_count = 0
    
    for r in range(N):
        for c in range(N):
            home_count = 0
            for dr in range(-(K-1), K):
                for dc in range(-(K-1), K):
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:  # 도시를 벗어났으면
                        continue
                    if abs(dr) + abs(dc) >= K:  # 마름모의 바깥 범위이면
                        continue
                    if graph[nr][nc] == 0:  # 집이 아니면
                        continue
                    home_count += 1

            if home_count > max_home_count and home_count*M >= cost:
                max_home_count = home_count

    return max_home_count



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 최소 1개 이상의 집이 존재하므로
    answer = 1

    if N % 2 == 0:
        max_K = N + 1
    else:
        max_K = N
    # 위 수식을 삼항연산자로 표현하면 아래와 같다
    # max_K = N+1 if N % 2 == 0 else N

    for K in range(max_K, 1, -1):
        # K일 때, 커버할 수 있는 최대 집의 수를 return
        result = search_K(K, calc_cost(K))
        if answer > 1:
            break


    print(f'#{tc} {answer}')


# ------------------------------------------------------------------------
# 두번째 풀이방법

def calc_cost(K):
    return K*K+(K-1)*(K-1)

def search_K(K, cost):
    max_home_coutn = 0

    for r in range(N):
        for c in range(N):
            home_count = 0
            for dis in range(K):
                home_count += dp[r][c][dis]

            if home_count > max_home_count and home_count*M >= cost:
                max_home_count = home_count

    return max_home_count



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    answer = 1
    max_K = N+1 if N % 2 == 0 else N

    # dp[r][c][dis] = count(집의 수)
    dp = [[[0] * ((N-1) * 2 + 1) for _ in range(N)] for _ in range(N)]
    
    for home_r in range(N):
        for home_c in range(N):
            if graph[home_r][home_c] == 1:

                for r in range(N):
                    for c in range(N):
                        dp[r][c][abs(home_r-r)+abs(home_c-c)] += 1

    for K in range(max_K, 1, -1):
        result = search_K(K, calc_cost(K))
        if result:
            answer = result
            break

        
    print(f'#{tc} {answer}')
