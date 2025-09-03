from collections import deque

def fill_one():
    global d
    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()
        answer[y][x] = 1
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == '0':
                q.append((ny, nx))

    for a in answer:
        print(a)

    return

def fill_zero():
    global d
    
    return

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = [[0 for _ in range(m)] for _ in range(n)]

fill_one()
fill_zero()