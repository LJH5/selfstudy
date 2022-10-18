houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for house in houses:
    if house == 1:
        print('전력을 차단하지 말아주세요')
        break

# 그냥 별개가 돼버림
# if True:
#     print('hi')

else:  # 여기서 else 는 위에서 단 한번이라도 break 가 걸리지 않을 경우만 발동합니다.
    print('작업을 시작해도 될 것 같아요')