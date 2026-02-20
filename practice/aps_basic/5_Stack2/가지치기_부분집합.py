# [1, 2, 3, ..., 10]에서 합이 55인 부분집합의 개수를 찾되, 
# 가지치기로 불필요한 탐색 최소화

def f(i, k, s, t):  # i: 현재 원소 인덱스, k: 배열 크기, s: 현재까지의 합, t: 목표값
    global cnt
    global fcnt
    fcnt += 1   # 함수 호출 횟수 카운트 (성능 측정용)

    # 현재 합이 목표합을 초과했을 시
    if s > t:
        return
    # 목표합 달성 시
    elif s == t:
        cnt += 1
        return
    # 모든 원소 확인 완료 시
    elif i == k:
        return
    # 
    else:
        bit[i] = 1              # i번째 원소 포함
        f(i+1, k, s+A[i], t)    # A[i]를 포함한 채로 다음 원소로 감
        bit[i] = 0              # i번째 원소 미포함 
        f(i+1, k, s, t)         # A[i]를 미포함한 채로 다음 원소로 감


#A = [1,2,3,4,5,6,7,8,9,10]
N = 10
A = [ i for i in range(1, N+1)]

key = 5
cnt = 0
bit = [0]*N
fcnt = 0
f(0,N,0,key)
print(cnt, fcnt)      # cnt: 정답 수, 즉 합이 key인 부분집합의 수