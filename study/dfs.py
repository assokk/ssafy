def dfs(node):
    print(node)

    for next_node in graph[node]:
        dfs(next_node)


'''
그래프에서는 길이 서로 연결되어 있어서 되돌아가는 길도 존재함
그래서 반드시 방문 체크가 필요하다.
'''
def dfs(node):
    visited[node] = 1
    print(node)

    for next_node in graph[node]:
        if visited[next_node] == 0:
            dfs(next_node)