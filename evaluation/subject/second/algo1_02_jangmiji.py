T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = input()
    b = input()

    '''
    a: 컨베이어 벨트 / b: 만들려는 단어
    a 배열을 순회하며 b 배열의 요소를 가지고 있는지 탐색한다.
    이때, a 배열을 순회하는 시작점이 되는 idx를 1씩 증가시킴으로써 이미 지나온 a 배열을 재탐색하는 일이 없도록 한다.
    요소를 가지고 있을 경우, count를 1 증가시키며 해당 반복문을 빠져나온다. 이 과정을 반복한다.
    글자 수와 count 수가 같은지 비교하여 글자를 다 찾았는지 확인하고 마지막으로 찾은 글자의 위치를 result에 저장한다.
    '''

    idx = 0
    count = 0
    result = -1

    for i in range(M):
        for j in range(idx, N):
            idx += 1
            if a[j] == b[i]:
                count += 1
                break

        if count == M:
            result = idx - 1

    print(f'#{tc} {result}')