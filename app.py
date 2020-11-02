import pygame
import random
import time

pygame.init()

win_width = 500
win_height = 500

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5.5
        self.health = 25
    
    def draw(self, win):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))


class Platform(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.y = 33
        self.vel = 6
    
    def draw(self, win, num):
        if num == 0:
            self.start = 0
            self.end = 125

            pygame.draw.rect(win, (255,0,0), (125, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (250, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (375, self.y, self.width, self.height))

        if num == 1:
            self.start = 125
            self.end = 250

            pygame.draw.rect(win, (255,0,0), (0, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (250, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (375, self.y, self.width, self.height))

        if num == 2:
            self.start = 250
            self.end = 375

            pygame.draw.rect(win, (255,0,0), (0, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (125, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (375, self.y, self.width, self.height))

        if num == 3:
            self.start = 375
            self.end = 500
            
            pygame.draw.rect(win, (255,0,0), (0, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (125, self.y, self.width, self.height))
            pygame.draw.rect(win, (255,0,0), (250, self.y, self.width, self.height))
            


def redrawWin():
    pygame.draw.rect(win, (0, 0, 0), (0, 0, win_width, win_height))

    text = font.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (390, 10))
    player.draw(win)
    platform.draw(win, openPlat)

    if game_over:
        gameOver()
    
    if Exit:
        exit()

    pygame.display.update()


def gameOver():
    pygame.draw.rect(win, (0, 0, 0), (0, 0, win_width, win_height))

    deathText = fontLose.render("YOU LOST!", 1, (255, 255, 255))
    playAgainText = font.render("WOULD YOU LIKE TO PLAY AGAIN? (Y/N)", 1, (255, 255, 255))

    win.blit(deathText, (135, 150))
    win.blit(playAgainText, (15, 200))


def exit():
    exitText = font.render("Exiting...", 1, (255, 255, 255))
    win.blit(exitText, (190, 400))



player = Player(300, win_height - 55, 50, 50)
platform = Platform(125, 30)


score = 0
openPlat = 0
beginingPlat = True
font = pygame.font.SysFont('comicsans', 30, True)
fontLose = pygame.font.SysFont('comicsans', 50, True)

Exit = False
game_over = False
run = True
while run:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # movement
    if keys[pygame.K_a] and player.x > 0:
        player.x -= player.vel

    if keys[pygame.K_d] and player.x < win_width - player.width:
        player.x += player.vel

    if keys[pygame.K_y]:
        player.x = 225
        platform.y = 33
        score = 0
        run = True
        game_over = False
    
    if keys[pygame.K_n]:
        Exit = True
        run = False


    # check for collision
    if platform.y + platform.height - 2 == player.y:
        if not (player.x > platform.start and player.x + player.width < platform.end):
            game_over = True


    # platform generator
    if beginingPlat:
        openPlat = random.randint(0, 3)
        beginingPlat = False
    
    if platform.y == 501:
        openPlat = random.randint(0, 3)
        score += 1
        platform.y = 33
    
    else:
        platform.y += platform.vel
        
    redrawWin()