def solution(s):
    answer = []
    
    # 문자열로 표현된 집합을 원소별로 끊어서 리스트화
    s_to_l = s[2 : len(s) - 2].split('},{')
    s_to_l.sort(key= lambda x: len(x))       # 정렬 순서는 길이순
    
    # 각각의 부분집합을 set화
    set_list = []
    for element in s_to_l:
        # 그냥 set을 하면 ','도 원소로 인정되므로 제거
        set_list.append(set(element.split(',')))  
    
    # 부분 집합 별로 answer와 비교해 없는 원소 찾고 answer에 추가
    for item in set_list:
        one = set(item)
        two = set(answer)
        tmp = one.difference(two)
        
        answer.append(list(tmp)[0])   # 문제 로직상 항상 tmp는 1개뿐이므로 이렇게 적용 가능한 것임

    answer = list(map(int, answer))   # 모든 원소를 숫자로 변환
    
    return answer