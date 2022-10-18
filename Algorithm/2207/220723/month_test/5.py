def id_user_data_valid(user_data):
    if user_data['id'] != '' and user_data['passward'] != '':
        return True
    else:
        return False
print(id_user_data_valid({'id': '', 'passward': 'dfafe'}))