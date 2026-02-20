# 상, 하, 좌, 우 이동을 위한 방향 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_grid(start_x, start_y, grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # 1. 방문 여부 체크 리스트 (DFS와 동일)
    visited = [[False] * cols for _ in range(rows)]
    
    # 2. 큐 생성 및 시작 노드 삽입
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    print(f"--- 2차원 배열 BFS 탐색 시작 ---")
    
    while queue:
        # 큐에서 현재 좌표 꺼내기
        x, y = queue.popleft()
        print(f"({x}, {y}) 방문", end=" -> ")
        
        # 3. 현재 위치에서 상하좌우 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 지도 범위 내에 있는지 확인
            if 0 <= nx < rows and 0 <= ny < cols:
                # 벽(1)이 아니고 아직 방문하지 않았다면
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 실행을 위한 메인 블록
if __name__ == "__main__":
    # 0: 길, 1: 벽
    matrix = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    # (0, 0) 지점에서 BFS 시작
    bfs_grid(0, 0, matrix)
    print("탐색 종료")