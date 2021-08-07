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
def backTrack(board):
    find = find_empty(board)
    if not find:
        return True;
    else:
        row, col = find;
    for i in range(1,10):
        if(check_number(board,i,(row,col))):
            board[row][col] = i;
            if(backTrack(board)):
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
                buttons.append(Button(font, (0,255,255), (i*39, j*39, i*39+39, j*39+39), str(board[j][i])))
            else:
                buttons.append(Button(font, (0,255,255), (i*39, j*39, i*39+39, j*39+39), ""))

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


def change_color(pos):
    pass
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
            change_color(pos)
            for button in buttons:
                if(button.is_clicked(pos)):
                    button.color = (0,0,0)
                    button.render(canvas)
        if event.type == pygame.KEYDOWN:
            buttons = draw_board(font, canvas)
    
    
    
    
    for i, button in enumerate(buttons):    
        button.render(canvas)
    draw_lines(canvas, 350,350)
    
    
    window.blit(canvas, (25,25))


    

    #canvas.fill((0, 255, 255))
    pygame.display.update()

pygame.quit()

'''print_board(board)
backTrack(board)
print("\n")
print("\n")
print_board(board)'''
