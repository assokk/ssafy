# import sys

# # 빠른 입력을 위한 설정
# input = sys.stdin.readline

# 상, 하, 좌, 우 이동
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def is_connectable(y, x, d, n, board):
    """현재 방향으로 전선을 연결할 수 있는지 확인"""
    ny, nx = y + dy[d], x + dx[d]
    while 0 <= ny < n and 0 <= nx < n:
        if board[ny][nx] != 0:
            return False
        ny += dy[d]
        nx += dx[d]
    return True

def fill(y, x, d, n, board, val):
    """전선을 깔거나(val=2) 치우는(val=0) 함수"""
    ny, nx = y + dy[d], x + dx[d]
    count = 0
    while 0 <= ny < n and 0 <= nx < n:
        board[ny][nx] = val
        count += 1
        ny += dy[d]
        nx += dx[d]
    return count

def dfs(idx, core_cnt, line_sum):
    global max_cores, min_lines

    # 모든 코어를 확인한 경우 (기저 사례)
    if idx == len(cores):
        if core_cnt > max_cores:
            max_cores = core_cnt
            min_lines = line_sum
        elif core_cnt == max_cores:
            min_lines = min(min_lines, line_sum)
        return

    # 현재 코어 좌표
    y, x = cores[idx]

    # 4방향 시도
    for d in range(4):
        if is_connectable(y, x, d, N, board):
            # 전선 설치
            length = fill(y, x, d, N, board, 2)
            dfs(idx + 1, core_cnt + 1, line_sum + length)
            # 전선 복구 (Backtracking)
            fill(y, x, d, N, board, 0)
    
    # 이 코어를 연결하지 않고 넘어가는 경우
    dfs(idx + 1, core_cnt, line_sum)

# 메인 실행부
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    cores = []
    
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(N):
            # 가장자리에 있는 코어는 이미 연결된 것으로 간주하므로 제외
            if row[j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    continue
                cores.append((i, j))

    max_cores = 0
    min_lines = float('inf')

    dfs(0, 0, 0)
    
    print(f"#{tc} {min_lines}")