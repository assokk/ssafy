def n_queen(r):
    global answer

    if r == N:
        answer += 1
        return
    
    for c in range(N):

        # 위쪽 검사
        if c in visited:
            continue

        # 위쪽 대각 검사
        # 위에서 내려오니까 아래는 볼 필요 X
        # 열에서 하나 뽑을거니까 양옆도 X
        for test_r in range(r):
           if r - test_r == abs(c - visited[test_r]):  # 행 번호와 열 번호가 동일해지면
               break
        else:
            visited[r] = c
            n_queen(r+1)
            visited[r] = -1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    answer = 0

    # 0 ~ N-1 열을 돌거니까 이 사이 수는 쓰면 안됨
    # -1은 미방문 상태 -> 해당 행에 대해서 뽑지 않았음
    visited = [-1] * (N)

    # 0번(행)부터 뽑기 시작
    n_queen(0)

    print(f'#{tc} {answer}')