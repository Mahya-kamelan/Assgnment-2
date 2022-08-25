counter = 1
win = 0
draw = 0
lose = 0
points = 0

while counter <= 8:
    print('emtiaz match', counter, 'ra vared konid: ')
    res = int(input())
    if res == 3:
        win += 1
        counter += 1
        points += res
    elif res == 1:
        draw += 1
        counter += 1
        points += res
    elif res == 0:
        lose += 1
        counter += 1
    else:
        print(' your score should be between 0, 1 or 3 (0 for lose , 1 foe equal and 3 for win)')
print(' final score: ', points)
print(' numbers of winning: ', win)
print(' numbers of lose: ', lose)
print(' numbers of equal: ', draw)
