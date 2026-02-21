from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

    return visited[N-1][M-1]


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


print(bfs())