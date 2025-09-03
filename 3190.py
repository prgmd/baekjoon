n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[b-1][a-1] = 1

for b in board:
    print(b)

visited = []
move = []
l = int(input())
for _ in range(l):
    wait, direction = input().split()
    move.append([int(wait), direction])

print(move)