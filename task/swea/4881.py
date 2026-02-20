def f(i, N, s):
    


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    min_v = 10000
    cnt = 0

    for i in range(N):
        cnt += 1

        