def make_graph():
    n = int(input())
    customer = []

    for _ in range(n+1):
        y, x = map(int, input().split())
        customer.append((y, x)) 
    
    return customer
def find_min_adj(start, end):
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

    return min_arr, min_val

customer = make_graph()
# print(customer)


for i in range(len(customer)-1):
    arr, val = find_min_adj(customer[i], customer[i+1])
    print(arr, val)

    # if i > len(customer)-3:
    #     break

    min_val = 1e9
    for a in arr:
        temp = find_min_adj(a, customer[i+2])
        min_val = min(min_val, temp[1])
        print(temp)
