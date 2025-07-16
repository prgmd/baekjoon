def fish_change(graph):
    visited = set()

    for n in range(1, 17):
        for y, g in enumerate(graph):
            for x, j in enumerate(g):
                v, d = j
                if n == v and n not in visited:
                    visited.add(n)
                    graph = change(graph, d, x, y)
                    break
    return graph

def change(graph, d, x, y):
    global direction

    nx = direction[d][1] + x
    ny = direction[d][0] + y

    for _ in range(8):
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or graph[ny][nx][0] == 17:
            if d == 8:
                d = 1
                nx = direction[d][1] + x
                ny = direction[d][0] + y
            else:
                d += 1
                nx = direction[d][1] + x
                ny = direction[d][0] + y
            continue
        else:
            temp = graph[ny][nx]
            graph[ny][nx] = graph[y][x]
            graph[y][x] = temp
            return graph

def shark_can_move(graph, now):
    global direction
    arr = []

    y, x = now
    dx, dy = direction[graph[y][x][1]]

    arr.append(now)
    for i in range(4):
        nx = arr[i][1] + dx
        ny = arr[i][0] + dy
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or graph[ny][nx] == (0, 0):
            break
        else:
            arr.append((ny, nx))
    arr.remove(now)
    
    return arr

def shark_eat_fish(now, eat):    
    y, x = now
    val, dir = graph[y][x]
    eat += val
    graph[y][x] = (17, dir)
    
    print("상어가 먹은 그래프")
    for i in range(4):
        print(graph[i])
    print("")
    
    return eat

def backtracking(graph, now, eat):
    global max_eat

    print("백트래킹 접속")
    print("")

    y, x = now
    eat = shark_eat_fish(now, eat)
    print("현재 좌표는", now, "현재 먹은 양은", eat)
    print("")

    graph = fish_change(graph)
    arr = shark_can_move(graph, now)
    print("물고기가 움직인 그래프")
    
    for i in graph:
        print(i)
    print("")

    if not arr:
        print("좌표가", now, "일 때 최종 먹은 양은", eat, "-----------------------------")
        max_eat = max(max_eat, eat)
        return
    
    print("거치기 전", graph)
    
    for nxt in arr:     
        print("이동 가능한 경로", arr, "중에서 ", nxt, "로 이동 중")
        graph[y][x] = (0, 0)
        
        backtracking(graph, nxt, eat)
        print("거친 후:", graph)
        print("롤백")
        for i in graph:
            print(i)
        print("")
    
    print(arr)

    return

# 그래프 및 방향 설정
graph = []
arr1 = []
arr2 = []
f_i = 0
f_d = 0

for _ in range(4):
    arr1 = list(map(int, input().split()))
    for i in range(8):
        if i % 2 == 0:
            f_i = arr1[i]
        else:
            f_d = arr1[i]
            arr2.append((f_i, f_d))
    graph.append(arr2)
    arr2 = []

direction = dict()
d = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
for idx, val in enumerate(d):
    direction[idx+1] = val

# 실행
eat = 0
max_eat = 0
start = (0, 0)
backtracking(graph, start, eat)
print("최종 양", max_eat)