# 보호필름 - 조합 + 부분집합

def check():
    for c in range(W):
        count = 1
        success = False

        for r in range(1, D):
            if arr[r][c] == arr[r-1][c]:
                count += 1
            else:
                count = 1

            if count >= K:
                success = True
                break
        
        if not success:
            return False
        
    return True


def dfs(row, cnt):
    global answer

    # 가지치기
    if cnt >= answer:
        return

    # 모든 행 다 돌았으면
    if row == D:
        if check():
            answer = min(answer, cnt)
        return

    # 약품 안 썼을 때
    dfs(row+1, cnt)

    original = arr[row][:]

    # A 약품 사용
    arr[row] = [0]*W
    dfs(row+1, cnt+1)

    # B 약품 사용
    arr[row] = [1]*W
    dfs(row+1, cnt+1)

    arr[row] = original


T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(D)]

    answer = D

    # 이미 통과하는 경우
    if check():
        answer = 0
    else:
        dfs(0, 0)
    
    print(f'#{tc} {answer}')