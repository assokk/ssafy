from collections import deque

def bfs(r, c, time):
    q = deque()
    q.append((r, c, 1))
    visited[r][c] = 1

    place = 0
    
    while q:
        r, c, time = q.popleft()

        if time == L:
            continue

        for d in pipe[tunnel[r][c]]:
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:

                if visited[nr][nc] == 1:
                    continue

                next_pipe = tunnel[nr][nc]

                if next_pipe == 0:
                    continue

                if opposite[d] in pipe[next_pipe]:
                    visited[nr][nc] = 1
                    q.append((nr, nc, time+1))

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                place += 1
    
    return place



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

pipe = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}

opposite = [1, 0, 3, 2]


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    answer = bfs(R, C, 1)

    print(f'#{tc} {answer}')



# -----------------------------