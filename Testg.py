import pygame
from random import randint
BLACK = (0,0,0)

class TextArea():
    def __init__(self, x=0,y=0,width=10,height=0,color=None):
        self.rect = pygame.Rect(x, y, width, height)
        # цвет заливки - или переданный параметр, или общий цвет фона
        self.fill_color = color

    def set_text(self, text, font_size = 14, text_color = BLACK):
        self.text  = text
        self.image = pygame.font.Font(None, font_size).render(text, True, text_color)

    def draw(self, shif_x = 0, shift_y = 0):
        pygame.draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image,(self.rect.x+shif_x, self.rect.y+shift_y) )


quest_card = TextArea(120,100, 290, 70, (136, 207, 153))
quest_card.set_text('Question', 50)


#То же самое для ответа
answer_card = TextArea(120,200, 290, 70, (136, 207, 153))
answer_card.set_text('Answer', 50)


quest_card.draw(10,10)
answer_card.draw(10,10)
clock = pygame.time.Clock()
while True:
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_q:
               number = randint(1,3)
               if number == 1:
                   quest_card.set_text('Ты жив?', 25)
               if number == 2:
                   quest_card.set_text('Ты жив?', 25)
               if number == 3:
                   quest_card.set_text('Ты жив?', 25)


    quest_card.draw(10, 10)
    answer_card.draw(10, 10)
    clock.tick(15)

