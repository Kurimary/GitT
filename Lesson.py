from pygame import *

class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 74))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.left = False
        self.right = False
        self.attack = False
        self.jump = False
        self.anim_count = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.left = True
            self.rect.x -= self.speed
        elif keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.right = True
            self.rect.x += self.speed
        else:
            self.right = False
            self.left = False
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            self.jump = True
        else:
            self.jump = False
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

        if keys[K_SPACE]:
            self.attack = True
        else:
            self.attack = False




# класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.png"), (win_width, win_height))

player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, xcor, ycor):

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))


animations = [image.load('run-00.png'),image.load('run-01.png'),image.load('run-02.png'),
              image.load('run-03.png'),image.load('run-04.png'),image.load('run-05.png'),]

animations_attack = [image.load('attack2-00.png'),image.load('attack2-01.png'),image.load('attack2-02.png'),
                   image.load('attack2-03.png'),image.load('attack2-04.png'),image.load('attack2-05.png'),]

animations_jump = [image.load('jump-00.png'),image.load('jump-01.png'),image.load('jump-02.png'),
                   image.load('jump-03.png'),]

base_pose = [image.load('idle-00.png'),image.load('idle-01.png'),image.load('idle-02.png'),
             image.load('idle-00.png'),image.load('idle-01.png'),image.load('idle-02.png')]
finish = False
clock = time.Clock()
FPS = 30
# in while -- clock.tick(FPS)

font.init()
font = font.Font('Sakura Blossom.ttf', 70)
win = font.render('Количество сбитых!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))
anim_count = 0

def draw_anim():
    global anim_count
    if anim_count +1 >= len(animations)*5:
        anim_count = 0
    if player.left:
        player.image = animations[anim_count//5]
        anim_count +=1
    elif player.right:
        player.image = animations[anim_count // 5]
        anim_count+=1
    elif player.attack:
        player.image = animations_attack[anim_count // 5]
        anim_count+=1
    elif player.jump:
        if anim_count +1 >= 20:
            for i in range(40):
                player.rect.y += 2
            anim_count = 0
        player.image = animations_jump[anim_count // 5]
        anim_count+=1
    else:

        player.image = base_pose[anim_count // 5]
        anim_count+=1

game = True
while game:
    window.fill((200, 200, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))

    win = font.render('Количество сбитых!', True, (255, 215, 0))
    lose = font.render('YOU LOSE!', True, (180, 0, 0))

    draw_anim()
    display.update()
    clock.tick(FPS)
