arr = [1, 2, 3]

for i in range(1 << len(arr)):
    sel = []
    for j in range(len(arr)):
        if i & (1 << j):
            sel.append(arr[j])
    print(sel)