import pygame
import random
import math

pygame.init()
score=0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Shooting_gallery_icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font(None, 36)
target_image = pygame.image.load("img/target_80.png")
target_width = 80
target_height = 80
radius = math.sqrt(target_width**2+target_height**2)
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
last_mouse_x, last_mouse_y = pygame.mouse.get_pos()
mouse_speed = 0
clock = pygame.time.Clock()
def move_target_away():
    global  last_mouse_x, last_mouse_y, mouse_speed, target_x, target_y, radius
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_speed = math.hypot(mouse_x - last_mouse_x, mouse_y - last_mouse_y)
    target_center_x, target_center_y = target_x + target_width/2, target_y + target_height/2
    mouse_distance = math.hypot(target_center_x - mouse_x, target_center_y - mouse_y)
    if mouse_distance < radius:
        angle = math.atan2(target_center_y - mouse_y, target_center_x - mouse_x)
        move_distance = max(0, 10 - mouse_speed /0.9)
        target_x += move_distance * math.cos(angle)
        target_y += move_distance * math.sin(angle)

        if target_x > SCREEN_WIDTH - target_width:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
        if target_x < 0:
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
        if target_y > SCREEN_HEIGHT - target_height:
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        if target_y < 0:
            target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    last_mouse_x, last_mouse_y = mouse_x, mouse_y

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1

    move_target_away()
    screen.blit(target_image, (target_x, target_y))
    score_text = font.render(f'Счет: {score}', True, (255, 255, 255))  # White color
    screen.blit(score_text, (10, 10))  # Position the score at the top-left corner
    pygame.display.update()
    clock.tick(60)
pygame.quit()
