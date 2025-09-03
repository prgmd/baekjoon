from itertools import combinations
from collections import deque
import copy

def find_min_val(viruses):
    global graph
    global total_road
    q = deque()
    visited = set()
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_val = 0

    temp_g = copy.deepcopy(graph)
    for virus in viruses:
        y, x = virus
        temp_g[y][x] = 0 # 이건 없애도 될듯
        q.append((y, x))
        visited.add((y, x))

    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and temp_g[ny][nx] != '-' and (ny, nx) not in visited:
                temp_g[ny][nx] = temp_g[y][x] + 1
                max_val = max(max_val, temp_g[ny][nx])
                q.append((ny, nx))
                visited.add((ny, nx))

    if total_road == len(visited)-len(viruses):
        return max_val
    else:
        return 1e9

# 변수값 설정
n, m = map(int, input().split())
graph = []
virus_map = []
answer = 1e9
cnt = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    # 받은 값이 2일 경우 virus_map에 좌표 입력
    for j in range(n):
        if graph[i][j] == 2:
            virus_map.append((i, j))
            graph[i][j] = '*'
            cnt += 1
        if graph[i][j] == 1:
            graph[i][j] = '-'
            cnt += 1

total_road = (n*n) - cnt

for g in graph:
    print(g)

# 바이러스의 모든 좌표 중 모집단 m개를 추출해 최솟값 계산
for com in combinations(virus_map, m):
    answer = min(find_min_val(com), answer)

if answer == 1e9:
    print(-1)
else:
    print(answer)