import pygame
class Button:
    def __init__(self, font, color, rect, value):
        self.rect = rect
        self.color = color
        self.value = value
        self.font = font

    def is_clicked(self, pos):
        if self.rect[0] < pos[0]-25 and self.rect[0] + self.rect[2] > pos[0]-25:
            if self.rect[1] < pos[1]-25 and self.rect[1] + self.rect[3] > pos[1]-25:
                return True
        return False

	# Renders the button and the centered textx
    def render(self, screen):
        
        pygame.draw.rect(screen, self.color, self.rect)
        text = self.font.render((self.value), True, (0,0,0))
        screen.blit(text, (self.rect[0]+10, self.rect[1]+10))
        