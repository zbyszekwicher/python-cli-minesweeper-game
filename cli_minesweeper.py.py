from random import randrange as r
from time import sleep

board = [
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x'],
['x','x','x','x','x','x','x','x','x','x']
    ]
space = '\n'*20
boom =' ██╗██████╗░░█████╗░░█████╗░███╗░░░███╗██╗\n ██║██╔══██╗██╔══██╗██╔══██╗████╗░████║██║\n ██║██████╦╝██║░░██║██║░░██║██╔████╔██║██║\n ╚═╝██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║╚═╝\n ██╗██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║██╗\n ╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝\n\n'
bombs = []
puste_pola = []

for i in range(15):
    bombs.append([r(10),r(10)])

def PrintB():
    print('    a   b   c   d   e   f   g   h   i   j')
    n = 0
    for l in board:
        print(n,'| '+l[0]+' | '+l[1]+' | '+l[2]+' | '+l[3]+' | '+l[4]+' | '+l[5]+' | '+l[6]+' | '+l[7]+' | '+l[8]+' | '+l[9]+' |',n)
        n+=1
    print('    a   b   c   d   e   f   g   h   i   j')

def countBombs(x,y):
    n = 0
    for i in [[x-1,y-1], [x-1,y], [x-1,y+1], [x,y-1], [x,y+1], [x+1,y-1], [x+1,y], [x+1,y+1]]:
        if i in bombs:
            n+=1
    return n

def polaStyczne(x,y):
    x = [[x-1,y-1], [x-1,y], [x-1,y+1], [x,y-1], [x,y+1], [x+1,y-1], [x+1,y], [x+1,y+1]]
    #print(x)
    n = [0,1,2,3,4,5,6,7,8,9]
    for i in x:
        #print(i[0])
        if i[0] not in n:
            x.remove(i)

    for i in x:
        if i[1] not in n:
            x.remove(i)

    return x

playing = True
while playing:
    print(space)
    PrintB()

    correct = False
    n = ('0','1','2','3','4','5','6','7','8','9')
    m = ('a','b','c','d','e','f','g','h','i','j')
    while not correct:
        inp = input('\n type number (0-9) and letter (a-j)\n')
        if len(inp) == 2:
            if inp[0] in n and inp[1] in m or inp[0] in m and inp[1] in n:
                correct = True

    if inp[0] in n and inp[1] in m:
        x = int(inp[0])
        y = ['a','b','c','d','e','f','g','h','i','j'].index(inp[1])
    else:
        x = int(inp[1])
        y = ['a','b','c','d','e','f','g','h','i','j'].index(inp[0])

    if board[x][y] == '!':
        print(space)
        PrintB()
        inp2 = input('\ndo you want to unmark '+inp+'? (yes/no)')
        while inp2 not in ('yes','no'):
            inp2 = input('\ndo you want to unmark '+inp+'? (yes/no)')

        if inp2 == 'yes':
            board[x][y] = 'x'

    elif board[x][y] == 'x':
        board[x][y] = 'X'
        print(space)
        PrintB()
        inp3 = input('\n 1 - dig\n 2 - mark\n')
        while inp3 not in ('1','2'):
            print('\n'*20)
            PrintB()
            inp3 = input('\n 1 - dig\n 2 - mark\n')

        if inp3 == '2':
            board[x][y] = '!'
        elif inp3 == '1':
            if [x,y] in bombs:
                playing = False
                print('\n'*20)
                print(boom)
                for i in bombs:
                    board[i[0]][i[1]] = 'B'
                sleep(0.5)
                PrintB()
            else:
                n = countBombs(x,y)
                puste_pola = []
                if n == 0:
                    board[x][y] = ' '
                    puste_pola.append([x,y])
                else:
                    board[x][y] = str(n)

                # Odkrywanie przylegajacych pustych pol
                to_check = [[x,y]]
                for n in range(10):
                    for v in to_check:
                        for i in polaStyczne(v[0],v[1]):
                            if i[0]<=9 and i[1]<=9 and i[0]>=0 and i[1]>=0:
                                if countBombs(i[0],i[1]) == 0 and not [i[0],i[1]] in puste_pola:
                                    if not [i[0],i[1]] in bombs:
                                        board[i[0]][i[1]] = ' '
                                        puste_pola.append([i[0],i[1]])
                                        to_check.append([i[0],i[1]])
                        to_check.remove(v)

                # Odkrywanie pol z numerkami w okol pustych pol
                for i in puste_pola:
                    for p in polaStyczne(i[0],i[1]):
                        if p[0]<=9 and p[1]<=9 and p[0]>=0 and p[1]>=0:
                            if board[p[0]][p[1]] == 'x':
                                n = countBombs(p[0],p[1])
                                if n in range(1,10):
                                    board[p[0]][p[1]] = str(n)

    win = True
    for l in board:
        if 'x' in l:
            win = False
    if win:
        m = 0
        for l in board:
            for i in l:
                if i == '!':
                    m += 1
        if m == len(bombs):
            playing = False
            print('\nYOU WIN!\n')



input('enter to exit')
