def solution(enroll, referral, seller, amount):
    relation = {'center': ['', 0]}

    for man, recom in zip(enroll, referral):
        if recom == '-':
            relation[man] = ['center', 0]
        else:
            relation[man] = [recom, 0]

    for who, how in zip(seller, amount):
        revenue = how * 100
        current = who

        while current != 'center':
            changes = revenue // 10
            relation[current][1] += revenue - changes

            if changes < 1:
                break

            revenue = changes
            current = relation[current][0]

    answer = [relation[man][1] for man in enroll]

    return answer
