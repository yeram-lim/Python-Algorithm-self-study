def solution(genres, plays):
    answer = []
    info = {}
    for index in range(len(genres)):
        genre = genres[index]
        play = plays[index]
        if genre not in info:
            info[genre] = {
                'total' : play,
                'list' : [index]
            }
        else:
            info[genre]['total'] += play
            info[genre]['list'].append(index)

    sorted_info_list = sorted(info.items(), key = lambda item : item[1]['total'], reverse=True)

    for genre, info in sorted_info_list:
        sorted_index_list = sorted(info['list'], key = lambda index : (-plays[index], index))
        answer += sorted_index_list[:2]
    return answer

a = solution(["classic", "pop", "classic", "classic", ],[500, 600, 150, 800, ])
print('답',a)