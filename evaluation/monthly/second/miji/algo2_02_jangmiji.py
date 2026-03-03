def dfs(r, c):
    visited[r][c] = 1
    gold = arr[r][c]
    # size = 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0:
            if visited[nr][nc] == 0:
                gold += dfs(nr, nc)
                # size += dfs(nr, nc)

    return gold
    # return size

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    result = []
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0 and visited[r][c] == 0:
                result.append(dfs(r, c))

    result.sort()
    print(f'#{tc}', end = ' ')
    print(result[-1])