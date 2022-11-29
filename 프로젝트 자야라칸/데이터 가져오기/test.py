cast = {
  "gender": 2,
  "id": 7467,
  "known_for_department": "Directing",
  "name": "David Fincher",
  "original_name": "David Fincher",
  "popularity": 17.984,
  "profile_path": "/tpEczFclQZeKAiCeKZZ0adRvtfz.jpg",
  "credit_id": "631f0289568463007bbe28a5",
  "department": "Directing",
  "job": "Director"
}





print(type(cast))
if cast['known_for_department'] == 'Directing':
    if 'job' in cast.keys() and cast['job'] == 'Director':
        print(cast['name'])
