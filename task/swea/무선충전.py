'''
dr, dc  > 방향 이동
T  > TC 수
M  > 이동 횟수
N  > 배터리의 수
A, B  > A, B 이동 경로(델타의 인덱스)
human_rcs  > A(0), B(1) 좌표
BC_info  > 배터리의 정보(N개)
charge_idxs  > [ [A가 충전가능한 위치인덱스 모음], [B가 충전가능한 위치인덱스 모음] ]


1. 이동 > M번
    2. 이동한 위치에서 A, B 충전할 수 있는 충전소 파악
        - A, B ~ 충전소 간의 거리를 파악 > 해당 거리가 충전 범위 이내이면 충전 가능
	- 충전량 말고 충전소 번호를 저장
    3. 최적의 충전량 선택 > max
	ㄱ. A만 충전할 수 없는 경우
	     > B를 반복
	ㄴ. B만 충전할 수 없는 경우
	     > A를 반복
	ㄷ. A, B 둘 다 충전 가능한 경우
    4. max 누적
'''


# 1: 상, 2: 우, 3: 하, 4: 좌
dr = [0, 0, 1, 0, -1]
dc = [0, -1, 0, 1, 0]

T = int(input())

for tc in range(1, T+1):
    answer = 0

    # M: 이동 횟수
    # N: 배터리의 수
    M, N = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    human_rcs = [[1, 1], [10, 10]]

    # BC_info > N
    # 0, 1 > 좌표
    # 2 > 충전 범위
    # 3 > 충전량
    BC_info = [0] * N
    for i in range(N):
        BC_info[i] = list(map(int, input().split()))
    
    # 충전 > M+1  (초기 위치에서 충전할 수 있다는 조건)
    for time in range(M+1):

        # 충전 가능한 위치 탐색 - A, B
        charge_idxs = [[], []]
        # A, B 중 누구를 돌지 > 0 / 1
        # i : A인지 B인지 - 사람 번호
        for i in range(2):
            r, c = human_rcs[i]
            # 어떤 충전소인지 선택
            # j : 충전소 번호
            for j in range(N):
                BC_r, BC_c, coverage, charge_amount = BC_info[j]
                if abs(r - BC_r) + abs(c - BC_c) <= coverage:
                    charge_idxs[i].append(j) 

        # 최적 충전량 - ㄱ, ㄴ, ㄷ
        charge = 0
        # ㄱ. A가 충전할 수 없는 경우
        if not charge_idxs[0]:  # False 일 때
            for i in charge_idxs[1]:    # B만 반복
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]
        # ㄴ. B가 충전할 수 없는 경우
        elif not charge_idxs[1]:
            for i in charge_idxs[0]:    # A만 반복
                if BC_info[i][3] > charge:
                    charge = BC_info[i][3]
        # ㄷ. A와 B 모두 충전 가능한 경우
        else:
            # i : A의 충전소 번호
            for i in charge_idxs[0]:
                # j : B의 충전소 번호
                for j in charge_idxs[1]:
                    if i == j:
                        if BC_info[i][3] > charge:
                            charge = BC_info[i][3]
                    else:
                        if BC_info[i][3] + BC_info[j][3] > charge:
                            charge = BC_info[i][3] + BC_info[j][3]

        answer += charge

        # 마지막 충전소면 이동할 필요 없으므로
        if time == M:
            break

        # 이동
        human_rcs[0][0] += dr[A[time]]
        human_rcs[0][1] += dc[A[time]]

        human_rcs[1][0] += dr[B[time]]
        human_rcs[1][1] += dc[B[time]]

    
    print(f'#{tc} {answer}')