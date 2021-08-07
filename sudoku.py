import pygame
import pygame.gfxdraw
from button import Button
board = [
    [0,2,0,0,4,0,0,0,8],
    [0,0,3,0,0,0,0,5,0],
    [0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,9,4],
    [0,0,0,1,0,8,0,6,3],
    [0,5,0,0,0,0,7,0,0],
    [0,3,1,8,0,0,0,2,0],
    [0,0,0,9,7,3,0,0,0]
]
def backTrack(screen, board, font):
    find = find_empty(board)
    if not find:
        return True;
    else:
        row, col = find;
    update_screen(screen)
    for i in range(1,10):
        
        if(check_number(board,i,(row,col))):
            board[row][col] = i;
            
            if(backTrack(screen,board, font)):
                return True
            board[row][col] = 0;
    return False;""

def check_number(board, number, position):
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
    boxX = position[1] // 3
    boxY = position[0] // 3
    for i in range(boxY*3, boxY*3 + 3):
        for j in range(boxX * 3, boxX*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True

def print_board(board):
    for row in range(len(board)):
        if(row % 3 == 0 and row != 0):
            print("------------------------");
        for col in range(len(board[0])):
            if(col % 3 == 0 and col != 0):
                print(" | ", end="");

            if(col == 8):
                print(board[row][col]);
            else:
                print(str(board[row][col]) + " ", end="");

def find_empty(board):
    for emptyR in range(len(board)):
        for emptyC in range(len(board[0])):
            if(board[emptyR][emptyC] == 0):
                return emptyR, emptyC
    return None;


def draw_board(font, screen):
    buttons = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[j][i] != 0):
                buttons.append(Button(font, (0,255,255), (i*39, j*39, 39, 39), str(board[j][i])))
            else:
                buttons.append(Button(font, (0,255,255), (i*39, j*39, 39, 39), ""))

    return buttons
def draw_lines(screen,width,height):
    for i in range(int(width/9)):
        if(i%3 == 0):
            pygame.gfxdraw.line(screen, i * 39, 0, i*39, height, (255,0,0))
        else:
            pygame.gfxdraw.line(screen, i * 39, 0, i*39, height, (0,0,0))

    for j in range(int(height/9)):
        if(j%3 == 0):
            pygame.gfxdraw.line(screen, 0, j * 39, width, j*39, (255,0,0))
        else:
            pygame.gfxdraw.line(screen, 0, j * 39, width, j*39, (0,0,0))

def update_screen(screen):
    pygame.event.pump()
    buttons = draw_board(font, canvas)
    for i, button in enumerate(buttons):    
        button.render(screen)
    
    draw_lines(screen, 350,350)  
    
    
    window.blit(screen, (25,25))

    pygame.display.update()


def encrypt(position):
    start = (25,25)
    size = 39
    for j in range(1,10):
        for i in range(1,10):
            if position[0] <= (start[0]+size*i) and position[1] <= (start[1] + (size*j)) and position[0] > (start[0]+(size*(i-1)) and position[1] > start[1]+size*(j-1)):
                return j-1,i-1

pygame.init()
pygame.font.init()

font = pygame.font.Font(pygame.font.get_default_font(), 30)



window = pygame.display.set_mode((400,400))
canvas = pygame.Surface((350,350))

buttons = draw_board(font, canvas)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(encrypt(pos))
            for i,button in enumerate(buttons):
                if(button.is_clicked(pos)):
                    button.color = (255,0,0)
                    button.render(canvas)
        if event.type == pygame.KEYDOWN:
            for button in buttons:
                if event.key == pygame.K_1 and button.color == (255,0,0):
                    #button.value = "1"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 1 
                    
                    #button.color = (0,255,255)
                if event.key == pygame.K_2 and button.color == (255,0,0):
                    #button.value = "2"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 2 
                    #button.color = (0,255,255)
                if event.key == pygame.K_3 and button.color == (255,0,0):
                    #button.value = "3"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 3 
                    #button.color = (0,255,255)
                if event.key == pygame.K_4 and button.color == (255,0,0):
                   # button.value = "4"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 4 
                   # button.color = (0,255,255)
                if event.key == pygame.K_5 and button.color == (255,0,0):
                   # button.value = "5"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 5 
                  #  button.color = (0,255,255)
                if event.key == pygame.K_6 and button.color == (255,0,0):
                  #  button.value = "6"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 6 
                  #  button.color = (0,255,255)
                if event.key == pygame.K_7 and button.color == (255,0,0):
                  #  button.value = "7"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 7 
                  #  button.color = (0,255,255)
                if event.key == pygame.K_8 and button.color == (255,0,0):
                  #  button.value = "8"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 8 
                  #  button.color = (0,255,255)
                if event.key == pygame.K_9 and button.color == (255,0,0):
                   #$ button.value = "9"
                    board[encrypt(pos)[0]][encrypt(pos)[1]] = 9 
                  #  button.color = (0,255,255)
            if(event.key == pygame.K_r):
                backTrack(canvas, board, font)
                #buttons = draw_board(font, canvas)
    
        
    
    
    update_screen(canvas)

    
    

    #canvas.fill((0, 255, 255))
    pygame.display.update()

pygame.quit()

'''print_board(board)
backTrack(board)
print("\n")
print("\n")
print_board(board)'''
