
money_dict = {
        '오만원': [50000, 0], 
        '만원': [10000, 0], 
        '오천원': [5000, 0], 
        '천원': [1000, 0], 
        '오백원': [500, 0], 
        '백원': [100, 0], 
        '오십원': [50, 0], 
        '십원': [10, 0] 
    }

# a = []
# for i in money_dict.values():
#     a.append(i[1])
# print(*a)
a = []
a.extend(i for i in money_dict.values())
print(a)