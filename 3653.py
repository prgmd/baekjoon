import sys

# 세그먼트 트리의 크기는 (N+M) * 4 로 설정
# movie_pos는 각 영화의 현재 인덱스를 저장
# next_top_idx는 맨 위에 올릴 영화의 새로운 인덱스를 생성

def update(tree, node, start, end, index, value):
    """
    세그먼트 트리의 특정 인덱스 값을 업데이트하는 함수
    """
    if start == end:
        tree[node] = value
        return
    
    mid = (start + end) // 2
    if start <= index <= mid:
        update(tree, node * 2, start, mid, index, value)
    else:
        update(tree, node * 2 + 1, mid + 1, end, index, value)
    
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(tree, node, start, end, left, right):
    """
    세그먼트 트리의 특정 구간 합을 구하는 함수
    """
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    return query(tree, node * 2, start, mid, left, right) + query(tree, node * 2 + 1, mid + 1, end, left, right)

def solve():
    n, m = map(int, sys.stdin.readline().split())
    movies_to_watch = list(map(int, sys.stdin.readline().split()))
    
    # 가상 인덱스 공간의 총 크기
    MAX_SIZE = n + m
    
    # 세그먼트 트리와 영화의 현재 위치를 저장할 배열
    seg_tree = [0] * (4 * MAX_SIZE)
    movie_pos = [0] * (n + 1)
    
    # 초기 상태 설정: n번 영화부터 1번 영화까지 아래에서 위로 배치
    # n번 영화가 인덱스 1에, 1번 영화가 인덱스 n에 위치
    # 이후 m번의 쿼리 동안 인덱스 n+1, n+2, ... n+m 사용
    for i in range(1, n + 1):
        pos = n - i + 1
        movie_pos[i] = pos
        update(seg_tree, 1, 1, MAX_SIZE, pos, 1)
        print(seg_tree)
    print(movie_pos)
    
    # 새로 올라올 영화의 인덱스 카운터
    next_top_idx = n + 1
    
    results = []
    
    for movie in movies_to_watch:
        # 1. 현재 위치 찾기
        current_pos = movie_pos[movie]
        
        # 2. 위에 있는 영화 개수 세기
        # 현재 위치보다 높은 인덱스에 있는 모든 영화의 개수를 구함
        # 즉, (현재 위치 + 1) 부터 (최대 인덱스)까지의 구간 합
        count_above = query(seg_tree, 1, 1, MAX_SIZE, current_pos + 1, MAX_SIZE)
        results.append(str(count_above))
        
        # 3. 영화를 맨 위로 옮기기 (인덱스 업데이트)
        # 3-1. 기존 위치에서 제거
        update(seg_tree, 1, 1, MAX_SIZE, current_pos, 0)
        
        # 3-2. 새로운 맨 위 인덱스에 추가
        movie_pos[movie] = next_top_idx
        update(seg_tree, 1, 1, MAX_SIZE, next_top_idx, 1)
        
        # 다음 영화가 올라올 새로운 맨 위 인덱스 준비
        next_top_idx += 1

    print(" ".join(results))

# 테스트 케이스 수만큼 solve 함수 호출
T = int(sys.stdin.readline())
for _ in range(T):
    solve()