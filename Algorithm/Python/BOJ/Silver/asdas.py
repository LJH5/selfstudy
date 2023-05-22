# 5C3
arr = ['headgear', 'headgear', 'eyewear']
sel = [0, 0]


def combination(idx, sidx):
    if sidx == 2:  # sel 길이 범위를 벗어나면 sel이 확정됐다는 소리니까 print
        print(sel)
        return

    if idx == 3:  # 얘도 벗어나지 않아야 함
        return

    sel[sidx] = arr[idx]  # sidx가 가리키는 위치에 idx가 가리키는 재료를 넣음
    combination(idx+1, sidx+1)  # 첫번째로는 두개의 화살표가 동시에 오른쪽으로 가보고
    combination(idx+1, sidx)  # 두번째로는 arr 쪽 화살표만 혼자 가봄.


combination(0, 0)