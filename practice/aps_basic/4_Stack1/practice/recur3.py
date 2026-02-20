def f(i, N, V):
    if i == N:  # 끝까지 갔는데 V를 못찾은 경우. 앞서 인덱스 범위를 검증해주는 역할도 함.
        return 0
    elif A[i] == V:
        return 1
    else:
        return f(i+1, N, V)
    

N = 3
A = [3, 7, 6]
# V = 2
V = 6
ans = f(0, N, V)
print(ans)