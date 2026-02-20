dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_grid(x, y, grid, visited):
    # 1. 현재 위치 방문 처리
    visited[x][y] = True
    print(f"({x}, {y}) 방문", end=" -> ")

    # 2. 상하좌우 4방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 지도 범위 내에 있고, 벽(1)이 아니며, 아직 방문하지 않았다면 탐색
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == 0 and not visited[nx][ny]:
                dfs_grid(nx, ny, grid, visited)

# 실행을 위한 메인 블록
if __name__ == "__main__":
    # 5x5 크기의 2차원 리스트 (0: 길, 1: 벽)
    matrix = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    # 방문 여부를 체크할 동일한 크기의 2차원 리스트
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    print("--- 2차원 배열 DFS 탐색 시작 ---")
    # (0, 0) 지점에서 탐색 시작
    dfs_grid(0, 0, matrix, visited)
    print("탐색 종료")