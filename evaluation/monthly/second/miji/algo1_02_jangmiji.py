T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    xr = xc = 0
    count = 0
    monsters = []

    # 입력으로 받은 배열을 순회하며 술래를 찾아 저장
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                monsters.append((r, c))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 술래를 기준으로 배열을 순회하며 감시에 닿는 칸의 값을 1로 변경
    for xr, xc in monsters:
        for d in range(4):
            nr = xr + dr[d]
            nc = xc + dc[d]

            while 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1:
                if arr[nr][nc] == 0:
                    arr[nr][nc] = 1

                nr += dr[d]
                nc += dc[d]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                count += 1

    print(f'#{tc} {count}')