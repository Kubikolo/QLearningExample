import pygame
import time
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))
x = 0
y = 700
ded = [(600, 0), (100, 100), (300, 100), (600, 100), (0, 200), (300, 300), (600, 300), (100, 400), (400, 300), (400, 500), (700, 500), (200, 600), (500, 600), (700, 600), (100, 700), (200, 700), (500, 700)]
score = [(700, 300), (200, 400), (400, 700)]
better_score = [(100, 0), (700, 700)]


def init():
    global x, y
    global score
    global better_score
    score = [(700, 300), (200, 400), (400, 700)]
    better_score = [(100, 0), (400, 700), (700, 700)]
    x = 0
    y = 700
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 100, 100))
    pygame.draw.rect(screen, (255, 255, 0), (100, 0, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (200, 0, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 0, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (400, 0, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (500, 0, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (600, 0, 100, 100))
    pygame.draw.rect(screen, (0, 150, 0), (700, 0, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (0, 100, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (200, 100, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (300, 100, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (400, 100, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (500, 100, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (600, 100, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (700, 100, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (0, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (100, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (200, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (400, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (500, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (600, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (700, 200, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (0, 300, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (100, 300, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (200, 300, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 300, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (400, 300, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (500, 300, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (600, 300, 100, 100))
    pygame.draw.rect(screen, (255, 255, 0), (700, 300, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (0, 400, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (100, 400, 100, 100))
    pygame.draw.rect(screen, (255, 255, 0), (200, 400, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 400, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (400, 400, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (500, 400, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (600, 400, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (700, 400, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (0, 500, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (100, 500, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (200, 500, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 500, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (400, 500, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (500, 500, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (600, 500, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (700, 500, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (0, 600, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (100, 600, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (200, 600, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 600, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (400, 600, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (500, 600, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (600, 600, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (700, 600, 100, 100))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (100, 700, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (200, 700, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (300, 700, 100, 100))
    pygame.draw.rect(screen, (255, 255, 0), (400, 700, 100, 100))
    pygame.draw.rect(screen, (0, 0, 0), (500, 700, 100, 100))
    pygame.draw.rect(screen, (255, 255, 255), (600, 700, 100, 100))
    pygame.draw.rect(screen, (255, 255, 0), (700, 700, 100, 100))


def move_right(screen):
    global x
    global y
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
    x += 100


def move_left(screen):
    global x
    global y
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
    x -= 100


def move_up(screen):
    global x
    global y
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
    y -= 100


def move_down(screen):
    global x
    global y
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
    y += 100


def q_function(current_q, reward, estimated_reward):
    update_q = current_q + 0.05 * (reward + 0.95 * estimated_reward - current_q)
    return update_q


q_table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
running = True
init()
run = 1
repeat_x = 0
repeat_y = 700
while running:
    time.sleep(0.01)
    reward = 0
    if run % 10 == 0:
        repeat_x = x
        repeat_y = y
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 100, 100))
    pygame.display.update()
    qx = x
    qy = y
    action = -1
    if random.randint(1, 100) < 100/pow(run, 1/2):
        if random.randint(1, 4) == 1:
            move_up(screen)
            action = 0
        elif random.randint(1, 4) == 2:
            move_down(screen)
            action = 1
        elif random.randint(1, 4) == 3:
            move_left(screen)
            action = 2
        else:
            move_right(screen)
            action = 3
    else:
        if q_table[int(str(int(y/10 + x/100)), 8)].index(max(q_table[int(str(int(y/10 + x/100)), 8)])) == 0:
            move_up(screen)
            action = 0
        elif q_table[int(str(int(y/10 + x/100)), 8)].index(max(q_table[int(str(int(x/100 + y/10)), 8)])) == 1:
            move_down(screen)
            action = 1
        elif q_table[int(str(int(y/10 + x/100)), 8)].index(max(q_table[int(str(int(x/100 + y/10)), 8)])) == 2:
            move_left(screen)
            action = 2
        elif q_table[int(str(int(y/10 + x/100)), 8)].index(max(q_table[int(str(int(x/100 + y/10)), 8)])) == 3:
            move_right(screen)
            action = 3
    if (x, y) in ded:
        reward += -10
        init()
    elif x < 0 or y < 0 or x > 700 or y > 700:
        reward += -100
        init()
    elif (x, y) in score:
        reward += 30
        score.pop(score.index((x, y)))
    elif (x, y) in better_score:
        reward += 30
        better_score.pop(better_score.index((x, y)))
    elif (x, y) == (700, 0):
        reward += 100
        print("WIN")
        init()
    else:
        reward += 0.1
    if x == repeat_x or y == repeat_y:
        reward += -5
    q_table[int(str(int(qx / 100 + qy / 10)), 8)][action] = q_function(q_table[int(str(int(qx / 100 + qy / 10)), 8)][action], reward, max(q_table[int(str(int(x / 100 + y / 10)), 8)]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    run += 1
