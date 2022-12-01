# 달팽이는 하루에 A미터 올라가고 B미터 미끄러짐
# 정상인 V미터에 도달하면 미끄러 지지 않음
# 정상에 도달하려면 몇일이 걸리는가?


a, b, v = map(int, input().split())
gab = a - b

result = (v - b) // gab

if (v - b) % gab != 0:
    result += 1
print(result)