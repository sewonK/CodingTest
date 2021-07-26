from collections import defaultdict
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

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
        result = sorted(genre_play[genre], key = lambda x: (x[1]), reverse=True)
        if len(result) > 1:
            answer.append(result[0][0])
            answer.append(result[1][0])
        else :
            answer.append(result[0][0])
    return answer

print(solution(genres, plays))