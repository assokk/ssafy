# # 부분집합을 생성하는 백트래킹 알고리즘

# '''
# 재귀적으로 각 원소에 대해 "포함" 또는 "미포함" 결정
#   • k == n 이 되면 하나의 부분집합 완성 → process_solution 호출
#   • 아니면 후보를 생성하고 재귀 호출
# '''
# def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
#     c = [0] * MAXCANDIDATES  # 이번 단계에서 가능한 후보를 저장

#     if k == n:
#         process_solution(a, k)  # 답이면 원하는 작업을 한다
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k + 1, n)

# '''
# 각 원소마다 2가지 선택지 제공
#   • c[0] = True : 원소 포함
#   • c[1] = False: 원소 미포함
# '''
# def construct_candidates(a, k, n, c):  # 후보 추천
#     c[0] = True  # 원소의 포함 여부
#     c[1] = False
#     return 2

# '''
# 완성된 부분집합 출력
#   • a[i]가 True인 원소만 출력
# '''
# def process_solution(a, k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end=' ')
#     print()


# MAXCANDIDATES = 2   # 각 원소가 가질 수 있는 선택지 (0 또는 1)
# NMAX = 3            # 전체 원소의 최대 개수 (len(num))
# a = [0] * NMAX      # 현재까지의 선택 결과를 저장
# num = [1, 2, 3]
# backtrack(a, 0, 3)



a = [0] * 3
print(a)