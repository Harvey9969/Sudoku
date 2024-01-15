import random
import pygame
import sys
import keyboard
ld = []
pygame.init()
pygame.key.get_mods()
timer = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('Arial', 30)
WHITE = (255, 255, 255)
board = []
press = []
for i in range(9):
    board.append([]) 
    for j in range(9):
        board[i].append("  ")
def show():
    print('----------------------------------------------')
    for i in range (9):
        print('|', end='')
        for j in range (9):
            print(' '+board[i][j]+' |', end = '')
        row = str(i)
        if len(row) == 1:
            row = "0"+row
        print('', row)
        print('----------------------------------------------')
    print("  0    1     2    3    4    5    6    7    8")
WIDTH, HEIGHT = 810,810
SQUARE_SIZE = 900//9
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sudoku")
def showboard():
    for i in range(1, WIDTH//9+1):
        pygame.draw.rect(screen, 'black', [0, WIDTH/9*i, WIDTH, 5], 5)
    for i in range(1, 3):
        pygame.draw.rect(screen, 'black', [0, WIDTH//9*3*i, WIDTH, 10], 5)
    for i in range(1, WIDTH//9+1):
        pygame.draw.rect(screen, 'black', [WIDTH/9*i, 0, 5, WIDTH], 5)
    for i in range(1, 3):
        pygame.draw.rect(screen, 'black', [WIDTH//9*3*i,0 , 10, WIDTH], 5)
def check(a, b): #press[-1][0] and [1]
    la = []
    lb = []
    lc = []
    aa, bb, c, d = 0, 0, False, False
    for i in range(9):
        la.append(board[b][i])
        lb.append(board[i][a])
    la = [elem for elem in la if elem != '  ']
    lb = [elem for elem in lb if elem != '  ']
    for i in range(len(la)):
        la[i] = la[i][0]
    for i in range(len(lb)):
        lb[i] = lb[i][0]
    if len(la) == len(set(la)) and len(lb) == len(set(lb)):
        print('aaaaaaaaaaaaaaaaaaaaaaaa')
        c = True
    else:
        board[b][a] = '  '   
    if c:
        for dx, dy in ([1, 1], [1, 0], [0, 1], [0, 0]):
            for i in range(3):
                if (a+1+dx*i) % 3 == 0 and (b+1+dy*i) % 3 == 0:
                    #print(a+dx*i, b+dy*i, 'aaaaaaaaaaaaaaaa')
                    d = True
                    aa, bb = a+1+dx*i, b+1+dy*i
    if d and aa != 0 and bb != 0:
        for ddx, ddy in ([-1, 1], [-1, -1], [1, 1], [1, -1], [1, 0], [0, 1], [-1, 0], [0, -1], [0, 0]):
            try:
                lc.append(board[bb-2+ddy][aa-2+ddx])
            except:
                pass
            #print(board[b+1+dy*i-2+ddy][a+1+dx*i-2+ddx], 'board')
            print(aa-2+ddx, bb-2+ddy)
            print(lc)
            lc = [elem for elem in lc if elem != '  ']
            for i in range(len(lc)):
                lc[i] = lc[i][0]
        if len(lc) != len(set(lc)):
            print('bbbbbbbbbbbbbbbbbb')
            board[b][a] = '  '
            lc = lc[:-1]
                        
                            
for _ in range(20):
    i = random.randint(0, 8)
    j = random.randint(0, 8)
    ld.append([i, j])
    ld = list(set(tuple(sub) for sub in ld))
for i in ld:
    if board[i[1]][i[0]] == '  ':
        board[i[1]][i[0]] = str(random.randint(1, 9)) + "*"
        check(i[0],i[1])    

show()         
running = True
display = False
while running:
    timer.tick(fps)
    screen.fill('white')
    showboard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos 
            x, y = x//90, y//90
            press.append([x, y])
            print(x, y)
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if len(key_name) == 3:
                key_name = key_name[1:2]
            for i in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                if i == key_name and len(press) > 0 and board[press[-1][1]][press[-1][0]][-1] != '*':
                    board[press[-1][1]][press[-1][0]] = key_name + ' '
                    display = True
                    show()
                    check(press[-1][0], press[-1][1])
            if (key_name == 'backspace' or key_name == 'delete') and board[press[-1][1]][press[-1][0]][-1] != '*':
                board[press[-1][1]][press[-1][0]] = '  '
            
                
            
    for i in range(9):
        for j in range(9):
            img = font.render(board[i][j], True, 'Black')
            screen.blit(img, (j*90+35, i*90+35))
    if any('  ' in sublist for sublist in board):
        pass
    else:
        pygame.draw.rect(screen, 'Blue', [230, 400, 400, 70])
        img = font.render('Congratulation!', True, 'white')
        screen.blit(img,  (330, 410))

     
            
    
    #print(keyboard.is_pressed("4"))
    pygame.display.flip()
pygame.quit()