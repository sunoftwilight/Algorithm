direct = [(1, 0), (0, 1), (-1, -1)]


def solution(n):
    answer = []
    tri = [[0] * n for _ in range(n)]
    max_v = sum(list(range(1, n + 1)))
    
    num = 2
    direct_idx = 0
    ci, cj = 0, 0
    di, dj = direct[direct_idx]
    tri[0][0] = 1
    
    while num <= max_v:
        ni, nj = ci + di, cj + dj
        
        if 0 <= ni < n and 0 <= nj < n and not tri[ni][nj]:
            ci, cj = ni, nj
            tri[ci][cj] = num
            num += 1
        
        else:
            direct_idx = (direct_idx + 1) % 3
            di, dj = direct[direct_idx]
    
    slice_idx = 1
    for i in range(n):
        answer += tri[i][:slice_idx]
        slice_idx += 1
    
    return answer