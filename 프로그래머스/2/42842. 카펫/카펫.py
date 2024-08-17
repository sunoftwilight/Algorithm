def solution(brown, yellow):
#     h w
#     yellow = (h-2) * (w-2) = hw - 2h - 2w + 4
#     brown = w * 2 + (h-2) * 2 = 2h + 2w - 4
    
#     brown + yellow = hw = 12
#     brown - yellow = -hw + 4(h + w) - 8  = -8
    
    answer = []
    
    summ = brown + yellow
    diff = brown - yellow
    
    h_sum_w = (diff + 8 + summ) / 4
    h_pro_w = summ
    
    for i in range(1, summ):
        if summ % i == 0:
            tmp = summ / i
            
            if i + tmp == h_sum_w:
                answer = [max(i, tmp), min(i, tmp)]
                
                return answer
