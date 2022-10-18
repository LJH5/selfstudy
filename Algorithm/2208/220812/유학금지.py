nuban = []
for i in 'CAMBRIDGE':
    nuban.append(i)

txt = input()

for j in nuban:
    if j in txt:
        txt = txt.split(j)
        txt = ''.join(txt)
print(txt)