initial_input = input().split()

spot = list(range(1, int(initial_input[0]) + 1))
line = int(initial_input[1])
start_spot = int(initial_input[2])
linelist = {}

# 그래프 저장하기
for i in range(line):
    line_input = input().split()
    key = int(line_input[0])
    value = int(line_input[1])

    # 키가 이미 존재하는 경우 리스트에 값을 추가
    if key in linelist:
        linelist[key].append(value)
    else:
        linelist[key] = [value]

    # 무방향 그래프일 경우 반대 방향도 추가
    if value in linelist:
        linelist[value].append(key)
    else:
        linelist[value] = [key]

# DFS 탐색
stack = [start_spot]
visited = set([start_spot])  # 방문한 노드를 추적하기 위해 집합을 사용
dfs_path = [start_spot]  # 방문한 경로를 저장하기 위한 리스트, 시작점을 바로 추가

linelist_copy = {k: v[:] for k, v in linelist.items()}  # linelist 복사본 생성

while stack:
    start_spot = stack[-1]
    
    # 현재 노드에서 연결된 노드들 중 아직 방문하지 않은 노드를 찾기
    found_unvisited = False
    if start_spot in linelist:
        for neighbor in sorted(linelist[start_spot]):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                dfs_path.append(neighbor)
                linelist[start_spot].remove(neighbor)  # 방문한 노드는 제거
                found_unvisited = True
                break
    
    if not found_unvisited:
        stack.pop()  # 더 이상 방문할 노드가 없으면 스택에서 제거

print(" ".join(map(str, dfs_path)))  # 방문한 경로 출력

# BFS
queue = [start_spot]
visited = set([start_spot])
bfs_path = [start_spot]

while queue:
    start_spot = queue.pop(0)
    
    if start_spot in linelist_copy:
        for neighbor in sorted(linelist_copy[start_spot]):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                bfs_path.append(neighbor)

print(" ".join(map(str, bfs_path)))
