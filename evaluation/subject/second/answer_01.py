T = int(input())

for tc in range(1, T+1):
    answer = 'NO'

    N, M = map(int, input().split())
    A = input()
    B = input()
    B_idx = 0

    for A_idx in range(N):
        if B[B_idx] == A[A_idx]:
            B_idx += 1
            if B_idx >= M:
                break
    
    if B_idx == M:
        answer = A_idx

    print(f'#{tc} {answer}')