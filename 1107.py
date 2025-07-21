from itertools import product

def find_min(l):
    global min_val
    global num_list

    for can_num in product(num_list, repeat = l):
        temp = ''

        for num in can_num:
            temp += str(num)
        
        min_val = min(min_val, abs(int(temp)-n) + len(str(int(temp))))

    return min_val

n = int(input())
error_cnt = int(input())

if error_cnt == 0:
    print(min(abs(100-n), len(str(n))))

elif error_cnt == 10:
    print(abs(100-n))

else:
    errors = list(map(int, input().split()))
    num_list = [i for i in range(10)]
    
    for error in errors:
        num_list.remove(error)
    
    min_val = abs(100-n)
  
    for length in range(1, 7):
        min_val = min(min_val, find_min(length))
    
    print(min_val)
