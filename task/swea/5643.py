

# 일단 기준점으로 1번부터 6번까지 돌기 (dfs 탐색을 진행할 기준 노드)

# dfsup에서는 해당 노드를 행으로 하는 arr에서 값이 1인 곳 찾기
# 찾았으면 cnt += 1, 방문처리 하고 해당 인덱스의 열을 행으로 가지는 곳을 탐색하면서 또 1 찾기

# dfsdown에서는 해당 노드를 행으로 하는 arr에서 값이 -1인 곳 찾기
# 찾았으면 cnt += 1, 방문처리 하고 해당 인덱스의 열을 행으로 가지는 곳을 탐색하면서 또 -1 찾기

# 총 cnt + 1 이 전체 학생 수와 같으면 자신의 키가 몇번째인지 알 수 있다는 뜻이므로 result += 1


T = int(input())

def dfsup(node):
    global cnt

    for i in range(1, N+1):
        if arr[node][i] == 1 and visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfsup(i)
    return cnt
        
def dfsdown(node):
    global cnt

    for i in range(1, N+1):
        if arr[node][i] == -1 and visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfsdown(i)
    return cnt



for tc in range(1, T+1):
    N = int(input())
    M = int(input())

    arr = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(N):
        i, j = map(int, input().split())
        arr[i][j] = 1
        arr[j][i] = -1

    visited = [0] * (N+1)
    dfsup(1)
    dfsdown(1)


    



    # 인접리스트