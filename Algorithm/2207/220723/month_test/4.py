weathers = [[35, 32], [33, 30]]
def turn(weathers):
    dict_temper = {'maximum':[], 'minimum':[]}
    for temper in weathers:
        dict_temper['maximum'].append(max(temper))
        dict_temper['minimum'].append(min(temper))
    return dict_temper

print(turn(weathers))