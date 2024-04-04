# 내 코드
# def solution(genres, plays):
#     answer = []
#     N = len(genres)
#
#     sep_genres = {}
#     for i in range(N):
#         if not sep_genres.get(genres[i]):
#             sep_genres[genres[i]] = [0]
#
#         sep_genres[genres[i]].append((plays[i], i))
#         sep_genres[genres[i]][0] += plays[i]
#
#     sorted_genres = []
#     for key, value in sep_genres.items():
#         sorted_genres.append((value[0], key))
#
#     sorted_genres.sort(reverse=True)
#
#     for data in sorted_genres:
#         tmp = sep_genres[data[1]][1:]
#         sort_tmp = sorted(tmp, key=lambda x: (x[0], -x[1]))
#         print(sort_tmp)
#
#         if len(sort_tmp) <= 1:
#             answer.append(tmp.pop()[1])
#         else:
#             for j in range(2):
#                 idx = sort_tmp.pop()
#                 answer.append(idx[1])
#
#     return answer


# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]

# genres = ["classic", "classic", "classic"]
# plays = [1, 1, 1]


# gpt 코드
def solution(genres, plays):
    answer = []
    sep_genres = {}

    # 장르별로 분리하고 재생 횟수 및 고유 인덱스를 기록
    for i, (genre, play) in enumerate(zip(genres, plays)):
        print(i, genre, play)
        if genre not in sep_genres:
            sep_genres[genre] = []

        sep_genres[genre].append((play, i))

    print(sep_genres)

    # 장르별로 재생 횟수 순서 및 고유 인덱스 순서로 정렬
    for genre in sep_genres:
        sep_genres[genre].sort(key=lambda x: (-x[0], x[1]))

    print(sep_genres)
    # 재생 횟수가 많은 장르 순서로 선택 후, 최대 2개의 곡 선택
    sorted_genres = sorted(sep_genres.keys(), key=lambda x: sum(p for p, _ in sep_genres[x]), reverse=True)
    print(sorted_genres)

    for genre in sorted_genres:
        answer.extend([idx for _, idx in sep_genres[genre][:2]])

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [800, 600, 150, 800, 2500]
print(solution(genres, plays))
