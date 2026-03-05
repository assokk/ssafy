from collections import deque
import copy
import sys
sys.setrecursionlimit(10**6)

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


def soonten(cnt):
    global answer

    if cnt == N:
        graph = copy.deepcopy(graph_original)

        for c in soonten_list:
            for r in range(H):
                if graph[r][c] != 0:
                    crush((r, c, graph[r][c]))

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
                    break
                        
        remain = W * H

        for i in range(H):
            remain -= graph[i].count(0)
            print(graph[i].count(0))
        print()


        if remain < answer:
            answer = remain

        return
    
    for i in range(W):
        soonten_list.append(i)
        soonten(cnt+1)
        soonten_list.pop()



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph_original = [list(map(int, input().split())) for _ in range(H)]
    answer = W * H

    soonten_list = []
    graph = copy.deepcopy(graph_original)

    soonten(0)

    print(f'#{tc} {answer}')