gomgom = list(map(int, input().split()))
ticket = list(map(int, input().split()))
total_gomgom = sum(gomgom)
for i in range(3):
    if ticket[i] - gomgom[i] > 0:
        ticket[i] -= gomgom[i]
        gomgom[i] = 0
        if i < 2:
            chang = ticket[i]//3
            ticket[i] -= chang*3
            ticket[i+1] += chang
    elif ticket[i] - gomgom[i] == 0:
        ticket[i] = 0
        gomgom[i] = 0
    else:
        gomgom[i] -= ticket[i]
        ticket[i] = 0
# print('ticket: ', ticket)
# print('gomgom: ', gomgom)

if ticket[2]//3 >= 1:
    chang = ticket[2]//3
    ticket[2] -= chang*3
    if gomgom[0] >= chang:
        gomgom[0] -= chang
        ticket[0] -= chang

if ticket[0]//3 >= 1:
    chang = ticket[0]//3
    if gomgom[1] >= chang:
        gomgom[1] -= chang

print(total_gomgom - sum(gomgom))