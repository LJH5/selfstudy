restaurants = [{'id': 342342, 'user_rating': 4, 'name': '음식점', 'menus': ['김밥', '떡볶이', '순대'], 'location':'00동 00-00' },
              {'id': 123443, 'user_rating': 5, 'name': '음식점2', 'menus': ['김밥2', '떡볶이2', '순대2'], 'location':'00동 22-22' }]

def menu_count(restaurants):
    for res in restaurants:
        if res.get('name') == '음식점':
            print(res['name']) 
            return len(res['menus'])
            
print(menu_count(restaurants))

