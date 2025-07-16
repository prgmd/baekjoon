from collections import deque

def find_min_adj(c):
    temp_adj = [(c[0]+1,c[1]), (c[0]-1,c[1]), (c[0],c[1]+1), (c[0],c[1]-1)]
    temp_arr = []
    min_arr = []
    min_val = 1e9

    for adj in temp_adj:
        y = adj[0]
        x = adj[1]
        val = abs(point[0]-y)+abs(point[1]-x)
        min_val = min(min_val, val)
        temp_arr.append((y, x, val))

    for arr in temp_arr:
        if arr[2] == min_val:
           min_arr.append(arr)

    return min_arr

graph = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
customer = []
q = deque()

for _ in range(n+1):
    y, x = map(int, input().split())
    customer.append((y, x))

start = customer.pop(0)
point = start
answer = 0

for c in customer:
    print("customer =", c)
    temp_arr = find_min_adj(c)
    print(temp_arr) 

print(q)
print(answer)