# 1 ~ 10

# 1. make set - 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모
# 초기화 (배열의 idx = 자기 자신, 저장된 값 = 부모 / 부모로 자기 자신을 가지도록 데이터 추가)
parent = [i for i in range(10)]


# 2. find set - 내 부모를 찾아가는 과정
def find_set(x):
    if parent[x] == x:
        return x

    # 최상위 부모가 나올 때까지 재귀 호출
    # return find_set(parent[x])

    # 경로 압축
    # x의 부모를 대표자로 수정 (최상위 부모를 저장)
    parent[x] = find_set(parent[x])
    return parent[x]


# 3. union - 같은 집합으로 묶기
def union(x, y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        print("사이클 발생")
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 대표자 묶기
union(1, 0)     # 0, 1 하나의 집합으로 묶기
union(2, 3)     # 2, 3 하나의 집합으로 묶기

# 대표자 검색 (확인 - 하나로 묶인 집합 중 가장 작은 수가 부모가 되도록)
print(find_set(0))    # 0
print(find_set(1))    # 0
print(find_set(2))    # 2
print(find_set(3))    # 2

# 같은 그룹인지 판별
t_x = 0
t_y = 2

union(1, 3)

# 싸이클 발생
# : 이미 같은 집합에 속해 있는 원소를 한번 더 포함(union)
union(0, 2)

if find_set(t_x) == find_set(t_y):
    print(f'{t_x}와 {t_y}는 같은 집합에 속해 있습니다')
else:
    print(f'{t_x}와 {t_y}는 다른 집합에 속해 있습니다')

