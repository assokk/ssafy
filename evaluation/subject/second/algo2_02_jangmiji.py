T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    '''
    배열을 순회하며 요소가 0인 곳을 찾아 해당 칸을 기준으로 상, 하, 좌, 우 칸의 요소를 합한다.
    그 합이 나온 값 중 가장 큰 경우 max_sum에 저장된다.
    모든 배열을 순회할 때까지 위 과정을 반복한다.
    '''

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_sum = 0

    for r in range(N):
        for c in range(M):
            pari_sum = 0
            if arr[r][c] == 0:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M:
                        pari_sum += arr[nr][nc]
                if pari_sum > max_sum:
                    max_sum = pari_sum

    print(f'#{tc} {max_sum}')