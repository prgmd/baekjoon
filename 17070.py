n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

pipe_steps = [[0 for _ in range(n)] for _ in range(n)]
pipe_steps[0][0] = 1
pipe_steps[0][1] = 1