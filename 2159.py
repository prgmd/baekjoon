from collections import deque
from collections import defaultdict

def find_min_adj(start, end, idx):
    temp_adj = [(end[0]+1,end[1]), (end[0]-1,end[1]), (end[0],end[1]+1), (end[0],end[1]-1)]
    temp_arr = []
    min_arr = []
    
    min_val = 1e9

    for adj in temp_adj:
        y = adj[0]
        x = adj[1]
        val = abs(start[0]-y)+abs(start[1]-x)
        min_val = min(min_val, val)
        temp_arr.append(((y, x), val))

    for arr in temp_arr:
        if arr[1] == min_val:
           min_arr.append(arr[0])

    return (min_arr, idx+1)

def bfs(d, start):
    global customer

    for nxt in d[start]:
        find_min_adj()

    return


def make_graph():
    n = int(input())
    customer = []

    for _ in range(n+1):
        y, x = map(int, input().split())
        customer.append((y, x)) 
    
    return customer

customer = make_graph()
d = defaultdict()
start = customer.pop(0)
arr, idx = find_min_adj(start, customer[0], 0)
d[start] = arr
print(d)

bfs(d, start)

# q = deque()
# idx = 0
# val = 0
# q.append((customer.pop(0), val))

# while q:
#     now = q.popleft()
#     print(now[0], "에서", customer[idx], "으로 넘어갈 때 가짓수", end = ' ')
#     arr, idx, val = find_min_adj(now[0], customer[idx], idx)
#     print(arr, "최소값은", val)

#     min_val = 1e9
#     for a in arr:
#         q.append((a, val))

    # for a in arr:
    #     q.append(a)
    # customer.pop(0)



# start = customer.pop(0)
# q = deque()
# answer = 0
# idx = 0
# temp_arr, idx_val, min_val = find_min_adj(start, customer[0], idx, 0)
# customer.pop(0)

# for c in customer:
#     for arr in temp_arr:
#         arr_val, idx_val, min_val = find_min_adj(arr, c, idx, min_val)
#     print(arr_val, idx_val, min_val)
#     start = c
#     idx = idx_val

# print(answer)

# first = customer[0]
# temp_arr = find_min_adj(start, first)
# print(temp_arr)
# for arr in temp_arr:
#     q.append(arr)

# while q:
#     first_adj = q.popleft()
#     temp_arr = find_min_adj(first_adj, customer[1])
#     print(temp_arr)

# # for c in customer:
# #     print("customer =", c)
# #     temp_arr = find_min_adj(c)
# #     for arr in temp_arr:
# #         q.append(arr)

#     print(q)