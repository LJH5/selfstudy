croatian = ['dz=', 'c=', 'c-', 'd-', 's=', 'z=', 'lj', 'nj']
txt = input()
cnt = len(txt)
for i in croatian:
    cnt -= txt.count(i)
print(cnt)