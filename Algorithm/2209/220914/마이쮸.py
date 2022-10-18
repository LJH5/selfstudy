# 튜플구조
# 키는 사람, 줄 선 횟수 ,받은 마이쮸 갯수 합
# (p, 0, 0)
p = 1

Q = []
N = 20  # 마이쮸 개수
m = 0   # 나눠준 개수

while m < N:
    Q.append((p, 1, 0))         # 대기줄에 넣음 초기에는 1번 줄서고 마이쮸 0개 있음
    v, c, my = Q.pop(0)         # 맨앞에 1명
    m += c                      # 줄선 횟수만큼 마이쮸를 줌
    Q.append((v, c+1, my+c))    # 줄선 횟수+1, 마이쮸 개수 + 줄선 횟수
    p += 1
print(f'마지막 받은 사람: {v}')