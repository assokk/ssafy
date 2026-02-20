from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    q = deque()
    visited = [[0] * 16 for _ in range(16)]

    visited[r][c] = 1   # 대기열에 넣어줄 때 방문체크
    q.append((r, c))
    
    
    while q:    # q가 빌 때까지 돌아라
        r, c = q.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if nr < 0 or nr >= 16 or nc < 0 or nc >= 16:
                continue
            if graph[nr][nc] == 1 or visited[nr][nc]:   # 벽이거나 방문했을 때
                continue
            if graph[nr][nc] == 3:
                return 1
            
            visited[nr][nc] = 1
            q.append((nr, nc))

    # 출구를 발견하지 못했을 때
    return 0


T = 10

for tc in range(1, T+1):
    input()
    graph = [list(map(int, input().split())) for _ in range(16)]
    r, c, goal_r, goal_c = -1, -1, -1, -1
    
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                r = i
                c = j
            elif graph[i][j] == 3:
                goal_r = i
                goal_c = j

    answer = bfs(r, c)