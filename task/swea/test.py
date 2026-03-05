from collections import deque

def crush(start):

    q = deque()
    q.append(start)

    while q:
        now_r, now_c, now_boom = q.popleft()
        graph[now_r][now_c] = 0

        for k in range(1, now_boom):
            for d in range(4):
                nr = now_r + dr[d] * k
                nc = now_c + dc[d] * k

                if 0 <= nr < H and 0 <= nc < W and graph[nr][nc] != 0:
                    if graph[nr][nc] > 1:
                        q.append((nr, nc, graph[nr][nc]))
                    elif graph[nr][nc] == 1:
                        graph[nr][nc] = 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

graph = [[1, 1, 1, 1, 1], [2, 1, 3, 1, 1], [1, 1, 1, 1, 1]]
N, W, H = 3, 5, 3

crush((1, 2, 3))


for c2 in range(W):
    temp = 0
    for r2 in range(H-1, -1, -1):
        if graph[r2][c2] == 0:
            temp += 1
        else:
            if temp == 0:
                continue
            graph[r2+temp][c2] = graph[r2][c2]
            graph[r2][c2] = 0


print(graph)