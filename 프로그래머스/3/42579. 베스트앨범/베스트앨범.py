def solution(genres, plays):
    answer = []
    sep_genres = {}

    # 장르별로 분리하고 재생 횟수 및 고유 인덱스를 기록
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in sep_genres:
            sep_genres[genre] = []
        sep_genres[genre].append((play, i))

    # 장르별로 재생 횟수 순서 및 고유 인덱스 순서로 정렬
    for genre in sep_genres:
        sep_genres[genre].sort(key=lambda x: (-x[0], x[1]))

    # 재생 횟수가 많은 장르 순서로 선택 후, 최대 2개의 곡 선택
    sorted_genres = sorted(sep_genres.keys(), key=lambda x: sum(p for p, _ in sep_genres[x]), reverse=True)
    for genre in sorted_genres:
        answer.extend([idx for _, idx in sep_genres[genre][:2]])

    return answer
