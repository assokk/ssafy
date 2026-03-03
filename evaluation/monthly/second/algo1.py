dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    answer = 0

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 술래 위치 찾기 & 0의 수를 세어주기
    chaser_rcs = []
    for r in range(N):
        for c in range(N):
            if graph[r][c] == 2:
                chaser_rcs.append((r, c))
            elif graph[r][c] == 0:
                answer += 1

    # 4방 탐색하면서 빈칸 메워주기 & answer를 조정 > 감시되는 위치
    # 4 방향, 술래 선정, 해당 방향으로 갈 수 있을 때까지
    for r, c in chaser_rcs:
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

        # 범위 안쪽 & 벽이 아니면
        while 0 <= nr < N and 0 <= nc < N and graph[nr][nc] != 1:
            if graph[nr][nc] == 0:
                graph[nr][nc] = 3
                answer -= 1

            nr += dr[dir]
            nc += dc[dir]

    print(f'{tc} {answer}')