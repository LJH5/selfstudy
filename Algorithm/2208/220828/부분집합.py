letters = ['a', 'b', 'c']

for i in range(1 << len(letters)):
    sel = []
    for j in range(len(letters)):
        if i & (1 << j):
            sel.append(letters[j])
    print(sel)