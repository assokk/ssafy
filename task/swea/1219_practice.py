T = 10

for tc in range(1, T+1):
    answer = 0  # 못 갔다고 가정
    adj_list = [[] for _ in range(100)]
    _, M = map(int, input().split())

    # info의 길이 = M * 2 (간선 하나 당 노드 두개 필요)
    info = list(map(int, input().split()))
    for i in range(0, M*2, 2):
        a, b = info[i], info[i+1]
        adj_list[a].append(b)

    print(adj_list)

    print(f'#{tc} {answer}')