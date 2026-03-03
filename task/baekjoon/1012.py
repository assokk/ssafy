def dfs(r, c):
    visited[r][c] = 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1 and visited[nr][nc] == 0:
                dfs(nr, nc)
                

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    visited = [[0] * M for _ in range(N)]

    result = 0

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and visited[r][c] == 0:
                dfs(r, c)
                result += 1
