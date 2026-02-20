
def bfs(r, c):
    visited[r][c] = 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and map[nr][nc] == 1
        







N = int(input())
map = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = 0

for r in range(N):
    for c in range(N):
        if map[r][c] == 1 and visited[r][c] == 0:
            bfs(r, c)