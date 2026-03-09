def dfs(cnt, left, right):
    global answer

    if cnt == N:
        answer += 1
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1

        dfs(cnt+1, left+weight[i], right)

        if right + weight[i] <= left:
            dfs(cnt+1, left, right+weight[i])

        visited[i] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    weight = list(map(int, input().split()))

    visited = [0] * N

    answer = 0

    dfs(0, 0, 0)

    print(f'#{tc} {answer}')