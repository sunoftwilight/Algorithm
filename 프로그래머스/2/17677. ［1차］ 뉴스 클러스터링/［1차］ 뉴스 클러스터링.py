def solution(str1, str2):
    answer = 0
    new1 = str1.upper()
    new2 = str2.upper()
    
    if new1 == new2:
        return 65536
    
    one = []
    for i in range(len(new1)-1):
        ele = new1[i : i + 2]
        print(ele)
        if ele[0].isalpha() and ele[1].isalpha():
            one.append(new1[i : i + 2])
    
    two = []
    for i in range(len(new2)-1):
        ele = new2[i : i + 2]
        if ele[0].isalpha() and ele[1].isalpha():
            two.append(new2[i : i + 2])
    
    one.sort()
    two.sort()
    union = list(set(two).union(set(one)))
    
    parent = 0
    son = 0
    
    for item in union:
        count1, count2 = one.count(item), two.count(item)
        parent += max(count1, count2)
        son += min(count1, count2)
    
    answer = int((son / parent) * 65536)
        
    return answer