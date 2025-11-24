from collections import defaultdict
def solution(genres, plays):
    albums = []
    gen = defaultdict(int) # 재생 횟수 총합
    musics = defaultdict(list) # 장르 별 음악
    genre_type = []
    popular_gen = ""
    for i, genre in enumerate(genres):
        gen[genre] += plays[i]
        musics[genre].append((i, plays[i]))
    sorted_gen = sorted(gen.items(), key = lambda item: item[1], reverse = True)
    genre_type.extend(items[0] for items in sorted_gen)
    for genre in genre_type:
        sorted_music = sorted(musics[genre], key = lambda item: (-item[1], item[0]))
        albums.extend(item[0] for item in sorted_music[0:2])
    return albums
        
    #popular_gen = max(gen.items(), key = lambda item: item[1])[0] # max()는 가장 큰 값을 가진 튜플 반환. 해당 튜플의 key값.
        
    