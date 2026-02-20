def f(i, N):    # A[i]에 접근하는 재귀함수
    if i == N:  # 모든 원소에 접근했으면
        return
    else:
        print(arr[i])
        f(i+1, N)   # 다음 원소 A[i+1]로 이동

A = [1, 2, 3]
f(0, 3)