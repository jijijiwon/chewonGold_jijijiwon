spot = int(input())
line = int(input())
start_spot = 1
linelist = {}

# 입력 처리에서 미리 정렬해 두는 방법
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

# 인접 리스트의 모든 이웃들을 미리 정렬
for key in linelist:
    linelist[key].sort()

# DFS 탐색
stack = [start_spot]
visited = set([start_spot])  # 방문한 노드를 추적하기 위해 집합을 사용
dfs_count = 0  # 감염된 노드 수를 세기 위한 변수

while stack:
    start_spot = stack[-1]
    
    found_unvisited = False
    if start_spot in linelist:
        for neighbor in linelist[start_spot]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                dfs_count += 1  # 감염된 노드 수 증가
                found_unvisited = True
                break
    
    if not found_unvisited:
        stack.pop()

print(dfs_count)
