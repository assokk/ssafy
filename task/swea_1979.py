T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for i in range(N):
        for j in range(N-K+1):
            r_sum = 0
            c_idx = 0
            for _ in range(K):
                r_sum += arr[i][j+c_idx]
                c_idx += 1
            if r_sum == K:
                if j > 0 and j + K < N:
                    if arr[i][j-1] == 0 and arr[i][j+K] == 0:
                        count += 1
                elif j > 0:
                    if arr[i][j-1] == 0:
                        count += 1
                elif j + K < N:
                    if arr[i][j+K] == 0:
                        count += 1
                else:
                    count += 1

    for j in range(N):
        for i in range(N-K+1):
            c_sum = 0
            r_idx = 0
            for _ in range(K):
                c_sum += arr[i+r_idx][j]
                r_idx += 1
            if c_sum == K:
                if i > 0 and i + K < N:
                    if arr[i-1][j] == 0 and arr[i+K][j] == 0:
                        count += 1
                elif i > 0:
                    if arr[i-1][j] == 0:
                        count += 1
                elif i + K < N:
                    if arr[i+K][j] == 0:
                        count += 1
                else:
                    count += 1

    print(f'#{tc} {count}')
