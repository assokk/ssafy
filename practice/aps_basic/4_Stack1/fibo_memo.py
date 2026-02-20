def fibo1(n) :
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0 :
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n = 20
'''
memo를 사용하지 않은 fibo.py는 n이 커질수록 cnt가 기하급수적으로 늘어나는 반면,
memo를 사용하면 n의 증가에 거의 비례하게 cnt가 증가함
'''
cnt = 0                 # 호출 횟수 기록
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo1(n), cnt)    # fibo.py와 count수 비교