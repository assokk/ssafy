def dfs(node):  # node: 현재 방문중인 node
    global answer
    visited[node] = 1   # 방문 체크 (stack에 들어올 때 = 함수 호출 시?) / 원복이 필요없는 경우 함수 내부에서 방문 체크 가능
    # visited는 answer와 달리 global 처리 안해도 됨
    if node == 99 or answer:    # answer: 백트래킹
        answer = 1
        return
    
    for next_node in adj_list[node]:
        # 방문 체크 되어있으면 건너 뛰자
        if visited[next_node]:
            continue

        # visited[next_node] = 1  # 원복 필요 시 방문 체크를 여기에서 하면 보기 좋음
        dfs(next_node)
        visited[next_node] = 0



T = 10

for tc in range(1, T+1):
    answer = 0  # 못 갔다고 가정
    _, M = map(int, input().split())

    # 이 숫자 입력의 길이는 M*2
    info = list(map(int, input().split()))
    adj_list = {}
    # ① adj_list = [[] for _ in range(100)]
    for i in range(0, M*2, 2):
        a, b = info[i], info[i+1]
        adj_list[a] = adj_list.get(a, [])
        # ① ↑ 삭제
        adj_list[a].append(b)
        # adj_list.get(a, []).append(b) 
        '''
        한줄로 작성 불가능한 이유
        값이 없다면 [] 반환, 그런데 []가 할당되어있지 않고 append의 return은 None이니까?
        '''

    visited = [0] * 100  # 0부터 99까지
    dfs(0)

    print(f'#{tc} {answer}')