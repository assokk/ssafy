# 보호필름 - 조합 + 부분집합
def dfs(row, cnt):

    # 모든 행 다 돌았으면
    if row == D:

    # 약품 안 썼을 때
    dfs(row+1, cnt)

    original = arr[row][:]

    # A 약품 사용
    arr[row] = [0]*W
    dfs(row+1, cnt+1)

    # B 약품 사용
    arr[row] = [1]*W
    dfs(row+1, cnt+1)

    arr[row] = original





T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(D)]
    
dfs(0, 0)

