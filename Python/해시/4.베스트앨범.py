from collections import defaultdict
genres = ["classic", "pop", "classic", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 800, 2500]

def solution(genres, plays):
    answer = []
    genre_play_total_cnt = defaultdict(lambda: 0)
    for genre, play in zip(genres, plays):
        genre_play_total_cnt[genre] += play
    genre_rank = [genre for genre, play in sorted(genre_play_total_cnt.items(), key = lambda x:x[1], reverse=True)]
    
    genre_play = defaultdict(lambda: [])
    for i in range(0, len(genres)):
        genre_play[genres[i]] += [[i, plays[i]]]
    
    for genre in genre_rank:
        # (x[1], x[0]) 아니고 x[1] 인 이유 -> 소팅 시 자동으로 key 값이 작은 순서대로 ?
        result = sorted(genre_play[genre], key = lambda x: (x[1]), reverse=True)
        print(result)
        if len(result) > 1:
            answer.append(result[0][0])
            answer.append(result[1][0])
        else :
            answer.append(result[0][0])
    return answer

print(solution(genres, plays))