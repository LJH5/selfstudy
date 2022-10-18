def is_id_valid(user_data):
    id = user_data['id']
    if id[-1].isdecimal():
        return True
    else:
        return False

print(is_id_valid({'id':'adfe1', 'passward':'djfien'}))