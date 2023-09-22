'''
Prim Algorithm

1. 시작 정점 초기화
2. 정점 갯수
    2-1. 최소 가중치를 가지는 간선 선택
    2-2. 방문 체크 (정점 선택)
    2-3. 가중치 갱신
'''

'''
Kruskal Algorithm 

- 간선의 배열로 저장 
    => parent 필요 (간선의 배열에 대한 가중치 정렬)
    => 사이클 형성 X (부모가 다른 애들끼리는 union)

- 간선 : V-1개 선택 필요 (V개의 정점 모두 방문해야 함)

'''


def find_set(x):
    if P[x] == x:
        return x

    else:
        return find_set(P[x])


def kruskal():
    # 0. 초기화
    total = 0
    cnt = 0     # 간선의 개수

    # 1. 간선의 배열 가중치 정렬
    edges.sort(key=lambda x: (x[2], x[0]))

    # 2. 간선을 V개 선택해야 한다 (정점 : 0 ~ V번 -> 총 V+1개)
    for i in range(E):
        # 2-1. 각 정점의 find_set 비교
        p1 = find_set(edges[i][0])
        p2 = find_set(edges[i][1])

        if p1 != p2:   # MST 포함
            # 2-1-1. union + 하고 싶은 일
            P[p2] = p1     # union
            total += edges[i][2]     # 가중치
            cnt += 1

        if cnt == V:
            return total


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    P = list(range(V+1))   # make-set

    print(f'#{tc} {kruskal()}')