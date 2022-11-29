import requests
import json


def get_movie_datas():
    total_data = []
    your_key = 'adffec049e1aaa9cfef0014e6f2ad451'
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 101):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={your_key}&language=ko-KR&page={i}"
        print(i, 'page')
        movies = requests.get(request_url).json()
        # print(movies)
        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'title': movie['title'],
                    'original_title': movie['original_title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'backdrop_path': movie['backdrop_path'],
                    'genres': movie['genre_ids'],
                    'adult': movie['adult'],
                    'movie_id': movie['id'],
                    'actors': [],
                    'director': None
                }
                actors = 0
                movie_credits = requests.get(f"https://api.themoviedb.org/3/movie/{fields['movie_id']}/credits?api_key={your_key}&language=ko-KR&page={i}").json()
                for cast in movie_credits['cast']:
                    fields['actors'].append(cast['name'])
                    actors += 1
                    if actors == 4:
                        break
                for member in movie_credits['crew']:
                    if member['known_for_department'] == 'Directing':
                        # print(cast['name'])
                        if 'job' in member.keys() and member['job'] == 'Director':
                            fields['director'] = member['name']
                            break
                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)
    print('*********성공*********')
    with open("movies.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\\t", ensure_ascii=False)


get_movie_datas()