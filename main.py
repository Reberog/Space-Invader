import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

# Player
player = pygame.image.load('spaceship.png')
player_x = 370
player_y = 480
player_change_x = 0
player_change_y = 0

score = 0
font = pygame.font.Font('freesansbold.ttf', 24)
txt_x = 10
txt_y = 10

clock = pygame.time.Clock()
time = 1600
tym_x = 650
tym_y = 10


def Time(x, y):
    tym = font.render('Time left: ' + str(int(time / 100)), True, (255, 255, 255))
    screen.blit(tym, (x, y))


def Score(x, y):
    scr = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(scr, (x, y))


def Player(x, y):
    screen.blit(player, (x, y))


# monster
monster = pygame.image.load('monster.png')
monster_x = random.randint(0, 736)
monster_y = random.randint(50, 200)
monster_change_x = 2.3
flag = 0


def Monster(x, y):
    screen.blit(monster, (x, y))


# bullet
bullet = pygame.image.load('bullet.png')
bullet_y = player_y
bullet_change = 0
bullet_x = 0
fire = "ready"


def Bullet(x, y):
    global fire
    fire = "fired"
    screen.blit(bullet, (x, y))


def hit(x1, y1, x2, y2):
    x = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if x < 20:
        return True


running = True
while running:

    if time < 0:
        running = False
    screen.fill((0, 0, 0))
    Time(tym_x, tym_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -3
            if event.key == pygame.K_RIGHT:
                player_change_x = 3
            if event.key == pygame.K_UP:
                player_change_y = -3
            if event.key == pygame.K_DOWN:
                player_change_y = 3
            if fire == "ready":
                if event.key == pygame.K_SPACE:
                    bullet_x = player_x
                    bullet_y = player_y
                    Bullet(bullet_x + 16, bullet_y)

        if event.type == pygame.KEYUP:
            player_change_x = 0
            player_change_y = 0

    # monster movement boundaries
    if monster_x <= 0:
        monster_change_x = 2.3
    if monster_x >= 769:
        monster_change_x = -2.3

    # defining boundaries
    if player_x <= 0:
        player_x = 0
    if player_x >= 736:
        player_x = 736
    if player_y <= 350:
        player_y = 350
    if player_y >= 480:
        player_y = 480

    player_x += player_change_x
    player_y += player_change_y
    monster_x += monster_change_x

    # Collision Logic
    if hit(monster_x, monster_y, bullet_x, bullet_y):
        score += 1
        monster_x = random.randint(0, 736)
        monster_y = random.randint(50, 200)
        Monster(monster_x, monster_y)
        fire = "ready"
        bullet_y = player_y
        Player(player_x, player_y)

    # bullet boundaries
    if fire == "fired":
        Bullet(bullet_x + 16, bullet_y)
        bullet_y -= 4

    if bullet_y < -32:
        fire = "ready"
        bullet_y = player_y

    Player(player_x, player_y)
    Monster(monster_x, monster_y)
    Score(txt_x, txt_y)
    time -= 1
    clock.tick(100)

    pygame.display.update()
