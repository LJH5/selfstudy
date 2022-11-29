import requests
import json


def get_movie_datas():
    total_data = []
    your_key = 'adffec049e1aaa9cfef0014e6f2ad451'
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    actors_set = set()
    director_set = set()
    movie_set = set()
    for i in range(1, 250):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={your_key}&language=ko-KR&page={i}&region=kr"
        print(i, 'page')
        movies = requests.get(request_url).json()
        # print(movies)
        for movie in movies['results']:
            print(movie['title'])
            movie_set.add(movie['id'])
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
                    actors += 1
                    if actors == 9:
                        break
                    fields['actors'].append(cast['id'])
                    if cast['id'] in actors_set:
                        continue
                    actors_set.add(cast['id'])
                    actor = requests.get(f"https://api.themoviedb.org/3/person/{cast['id']}?api_key={your_key}").json()
                    actor_fields = {
                        'name': actor['name'],
                        'aka': actor['also_known_as'],
                        'profile_path': actor['profile_path']
                    }
                    actor_data = {
                        'pk': actor['id'],
                        'model': "movies.actor",
                        'fields': actor_fields
                    }
                    total_data.append(actor_data)
                for member in movie_credits['crew']:
                    if member['known_for_department'] == 'Directing':
                        # print(cast['name'])
                        if 'job' in member.keys() and member['job'] == 'Director':
                            fields['director'] = member['id']
                            if member['id'] in director_set:
                                continue
                            director_set.add(member['id'])
                            director = requests.get(f"https://api.themoviedb.org/3/person/{member['id']}?api_key={your_key}").json()
                            director_fields = {
                                'name': director['name'],
                                'aka': director['also_known_as'],
                                'profile_path': director['profile_path']
                            }
                            director_data = {
                                'pk': director['id'],
                                'model': "movies.director",
                                'fields': director_fields
                            }
                            total_data.append(director_data)
                            break
                data = {
                    'pk': movie['id'],
                    'model': 'movies.movie',
                    'fields': fields
                }

                total_data.append(data)
    
    print('*********성공*********')
    with open("movies.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)


get_movie_datas()