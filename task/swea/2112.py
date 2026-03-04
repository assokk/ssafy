# N = 3
# numbers = [1, 2, 3, 4, 5]
# pick_numbers = []

# # count : 지금까지 고른 숫자 개수
# # idx : 다음의 탐색 시작 인덱스
# def comb(count, idx):
#     print(pick_numbers)
#     if count == N:
#         # 다 골랐을 때 작업
#         return
    
#     for i in range(idx, 5):
#         pick_numbers.append()
#         comb(count+1, i+1)


# comb(0, 0)

def test_film():
    for c in range(W):
        count = 0
        before = -1
        for r in range(D):
            if films[r][c] != before:
                count = 1
            else:
                count += 1
                if count >= K:
                    break
            before = films[r][c]

        if count < K:
            return False
    return True


def comb(count, idx):
    global answer

    if test_film():
        answer = count

    if count >= answer-1:
        return
    
    for i in range(idx, D):
        backup = films[i]
        films[i] = A
        comb(count+1, i+1)
        films[i] = B
        comb(count+1, i+1)
        films[i] = backup


T = int(input())
# 최댓값을 기준으로 설정해줘도 문제가 되지 않음
# 얕은 복사
A = [0] * 20
B = [1] * 210

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]
    answer = K

    comb(0, 0)
    print(f'#{tc} {answer}')