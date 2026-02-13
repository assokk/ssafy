dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    answer = 0
    
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(M):
            
            if flies[r][c] == 0:
                temp_sum = 0
                for dir in range(4):
                    nr = r+dr[dir]
                    nc = c+dc[dir]
                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        continue
                    temp_sum += flies[nr][nc]

                if answer < temp_sum:
                    answer = temp_sum

    print(f'{tc} {answer}')