def solution(data):
    # 감염된 컴퓨터의 수 초기화
    computer = 0
    # 총 컴퓨터 수 & 연결 정보 파싱하기
    lines = data.strip().split("\n")
    total_computers = int(lines[0])
    connections_count = int(lines[1]    )
    connections = [list(map(int, line.split())) for line in lines[2:2+connections_count]]

    # 네트워크 연결은 무방향 그래프로..
    # 인접 리스트 초기화
    graph = [[] for _ in range(total_computers + 1)]
    for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
    
    # 방문 기록 초기화
    visited = [False] * (total_computers + 1)

    def dfs(v):
        visited[v] = True
        for next in graph[v]:
            if not visited[next]:
                dfs(next)
    
    # 바이러스 1번 컴퓨터에서 시작하니까...
    dfs(1)

    # true = 1, false = 0 이니까 true 개수를 더한다고 생각해서! sum 사용
    # 1번 통해서 감염되니까 1은 빼주기..
    computer = sum(visited) - 1
    return computer

print(solution(
    """
7
6
1 2
2 3
1 5
5 2
5 6
4 7
    """
))