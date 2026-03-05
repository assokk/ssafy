def decimal_to_binary(n):
    binary_number = ""

    if n == 0:
        return "0"

    # 0보다 클 때까지 2로 나누면서
    # 나머지를 정답에 추가
    while n > 0:
        # 2로 나눈 나머지를 구해서
        remain = n % 2
        # 정답에 추가
        binary_numbrer = str(remain) + binary_number

        # 2로 나눈다
        n = n // 2

    return binary_number


# 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEFG"
    hexadecimal_number = ""

    while n > 0:
        remain = n % 16
        hexadecimal += hex_digits[remain]
        n = n // 16

decimal_to_hexadecimal(17)


# ------------------
# 54p

def func(binary_str):
    # 전달받은 문자열을 뒤에서부터 탐색
    # 10진수로 변환하면서 계산
    pass

# 문자열 입력
word = input().strip()

for i in range(0, len(word), 7):
    func(word[i:i+7])


# ------------------
# 비트 연산 응용

# 1.  1 << n -> 2 ^ n 을 구할 수 있다.
arr = [7, 1, 3, 5]

print(f"부분 집합의 수: {1 << len(arr)}개")

# 2.  전체 부분 집합을 구할 수 있다.
# i = 부분집합 번호
for i in range(1 << len(arr)):
    print(f"{i}번 째 부분집합: ", end = ' ')
    # subset = []
    # 각 자리수를 모두 확인
    for idx in range(len(arr)):
        if i & (i << idx):
            # subset.append(arr[idx])
            print(arr[idx], end=' ')
    # if len(subset) == 2:
        # result.append(subset)
    print()



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

    # 모든 행 선택 완료
    if row == D:
        if check():
            answer = min(answer, cnt)
        return

    # 1️⃣ 약품 안씀
    dfs(row+1, cnt)

    # 원래 행 저장
    original = arr[row][:]

    # 2️⃣ A 약품 (0)
    arr[row] = [0] * W
    dfs(row+1, cnt+1)

    # 3️⃣ B 약품 (1)
    arr[row] = [1] * W
    dfs(row+1, cnt+1)

    # 복구
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

    print(f"#{tc} {answer}")