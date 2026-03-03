from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global max_mining, count_block
    
    q = deque()
    visited = [[0]*N for _ in range(N)]

    q.append((r, c))   
    visited[r][c] = 1

    current_mining = 0
    current_count = 0
    
    while q:
        r, c = q.popleft()
        current_count += 1
        current_mining += graph[r][c]

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if nr < 0 or nr >= N or nc < 0 or nr >= N:
                continue
            if graph[nr][nc] == 0 or visited[nr][nc]:
                continue

            visited[nr][nc] = 1
            q.append((nr, nc))

    if current_mining > max_mining:
        max_mining = current_mining
        count_block = current_count
    elif current_mining == max_mining:
        if current_count < count_block:
            count_block = current_count


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    max_mining = 0
    count_block = 0

    for r in range(N):
        for c in range(N):
            if graph[r][c] != 0:
                bfs(r, c)

    print(f'#{tc} {max_mining} {count_block}')