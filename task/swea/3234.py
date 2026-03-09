# count: 뽑은 개수
# visited: 현재 뽑아 놓은 상태
# left, right: 왼쪽과 오른쪽의 무게
def dfs(count, visited, left, right):

    if count == N:
        return 1
    
    # 현재 방문 상태에서 left 무게를 이미 세었다면
    if dp[visited].get(left):
        return dp[visited][left]
    
    temp = 0
    for i in range(N):
        # i 번째 무게추를 골랐다면 건너뛰기
        if visited & (1 << i):
            continue

        temp += dfs(count+1, visited | (1 << i), left+weights[i], right)

        if left >= right+weights[i]:
            temp += dfs(count+1, visited | (1 << i), left, right+weights[i])

    
    # 현재 visited 상태에서 left 무게일 때의 경우의 수를 반환
    dp[visited][left] = temp
    return temp



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))

    dp = [{} for _ in range(2**N)]

    print(f'#{tc} {dfs(0, 0, 0, 0)}')


# 비트 마스킹 굳이 안하고 배열(튜플)로도 구현 가능




# '''
# numbers = [1, 2, 3, 4, 5]
# N = numbers 길이
# M = 뽑을 개수
# pick_numbers = 뽑은 숫자 보관

# N개 M개를 뽑아 줄 세우는 순열
# '''

# numbers = [1, 2, 3, 4, 5]
# N = len(numbers)
# M = 3

# pick_numbers = []
# def perm(count):
#     # 다 뽑으면 > count가 M개
#     if count == M:
#         print(*pick_numbers)
#         return
    
#     # 다 안뽑았다면
#     for i in range(N):
#         # 안 뽑은 숫자 중에서
#         if visited[i] == 1:
#             continue

#         visited[i] = 1
#         pick_numbers.append(numbers[i])
#         perm(count+1)
#         visited[i] = 0
#         pick_numbers.pop()

# visited = [0] * N

# perm(0)


# '''
# 경우의 수를 세는 법
# '''
# def perm(count):
#     # 다 뽑으면 > count가 M개
#     if count == M:
#         return 1
    
#     # 다 안뽑았다면
#     temp = 0
#     for i in range(N):
#         # 안 뽑은 숫자 중에서
#         if visited[i] == 1:
#             continue

#         visited[i] = 1
#         temp += perm(count+1)
#         visited[i] = 0
#     return temp

# answer = perm(0)