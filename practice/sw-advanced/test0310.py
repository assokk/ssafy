# ------------------------------------------- 12p
# 3명의 친구 부분집합 만들기
arr = ['O', 'X']
path = []

# 3명의 친구 : depth = 3
# O, X 중 하나 선택 : branch = 2
def recur(cnt):
    if cnt == 3:
        print(*path)
        return
    

    # O를 선택 (부분집합에 포함 되는 경우)
    path.append(arr[0])
    recur(cnt + 1)
    path.pop()

    # X를 선택 (안되는 경우)
    path.append(arr[1])
    recur(cnt + 1)
    path.pop()


recur(0)


# ------------------------------------------- 13p

name = ['MIN', 'CO', 'TIM']

def recur2(idx, subset):
    if idx == 3:
        print(*subset)
        return
    

    # 포함 하는 경우
    recur2(idx + 1, subset + [name[idx]])
    # 안 하는 경우
    recur2(idx + 1, subset)


recur2(0, [])



# ------------------------------------------- 16p
arr = [1, 2, 3, 4]
n = len(arr)

def get_subset1():
    # 1. 0 ~ 부분집합의 수 만큼 반복
    # - i : 부분집합의 번호
    for i in range(1 << n):
        # i를 이진수로 생각하고, 각 자리 수를 비교
        for idx in range(n):
            if i & (1 << idx):
                print(arr[idx], end=' ')
        print()


get_subset1()



# ------------------------------------------- 22p
# 5명 중 N명을 뽑을 것이다
arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []

# N명을 뽑는다 : depth = N
# 5명 중 하나를 선택 : branch = 5
# 1. 전체 순열 코드부터 시작
# 2. 직전 선택을 다음 재귀호출로 넘겨주고,
#    그 다음부터 선택하도록 구성
def recur(cnt, prev):
    if cnt == N:
        print(*path)
        return
    
    # 이전에 선택했던 것 다음거부터 탐색하자 (중복 제거된 조합)
    # prev + 1 -> prev 로 해주면 이전 선택을 허용하되, 순서에 따른 중복은 제거 (중복 조합)
    for i in range(prev + 1, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i)   # 이전 선택을 함께 전달
        path.pop()


recur(0, -1)    # 중복 제거
# recur(0, 0)     중복 허용
