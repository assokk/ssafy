from collections import deque

# 거리를 return
def bfs(S):
    q = deque()
    visited = [0] * (V+1)

    q.append(S)
    visited[S] = 1

    distance = 0

    while q:
        # 현재 큐에 있는 만큼 == 현 스텝에서 담긴 만큼
        for _ in range(len(q)):
            node = q.popleft()
            if node == G:
                return distance
            
            for next_node in adj_list[node]:
                if visited[next_node]:  # 방문체크 되어있으면
                    continue
                visited[next_node] = 1
                q.append(next_node)
        
        distance += 1
    return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    S, G = map(int, input().split())
    answer = bfs(S)

    print(f'#{tc} {answer}')