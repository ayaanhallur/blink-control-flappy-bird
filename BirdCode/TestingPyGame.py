
import pygame

import random

#Start Pygame
pygame.init()

#Window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Game")

tick=180
speed=tick/48

#Clock
clock = pygame.time.Clock()

#Player
player_size = 45


pipei = []

#Imports each pipe on a range from 1 to 6 (7 is exclusive)
for i in range(1, 7): 
    img = pygame.image.load(f"pipe_{i}tall.png").convert_alpha()
    img = pygame.transform.scale(img, (int(img.get_width() * HEIGHT / img.get_height()), HEIGHT))
    pipei.append(img)
    

#Player Images
original_image = pygame.image.load("Flappy_Bird_V3.png").convert_alpha()
player_image = pygame.transform.scale(original_image, (player_size, player_size))

image_2 = pygame.image.load("Flappy_Bird_Flap.png").convert_alpha()
player_image_2 = pygame.transform.scale(image_2, (player_size, player_size))


player = pygame.Rect(
    WIDTH // 2 - player_size // 2,
    HEIGHT // 2 - player_size // 2,
    player_size,
    player_size
)


#Player stats
gravity = 0.035
jump_power = 1.5
i=1
dt = 0
bird_y = float(player.y) #makes float because player only holds int

#Pipe Stats
pipes = []
pipe_speed = 2
spawn_timer = 0
next_spawn = random.randint(200, 400)

image_use = player_image

# Game loop
running = True

while running:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print ("jump"+str(i))
            i=i+1
            dt = -jump_power
            image_use = player_image_2
    dt += gravity

    if dt >= -1.5:
        image_use = player_image

    if (player.y<0.001):
        dt=0.1
        print ("roof"+str(dt))

    bird_y += dt
    player.y = round(bird_y)


    #Keep player inside window
    player.clamp_ip(screen.get_rect())

    #Background
    screen.fill((30, 30, 40))

    #Draw Player
    screen.blit(image_use, player)

    #Draw random Pipe
    spawn_timer += 1
    #Mask is used to allow collision with the pixels that are acutally colored in
    if spawn_timer >= next_spawn:
        img = random.choice(pipei)
        rect = img.get_rect(topleft=(WIDTH, 0))
        pipes.append({"image": img, "rect": rect, "x": float(WIDTH),"mask": pygame.mask.from_surface(img)})
        spawn_timer = 0
        next_spawn = random.randint(200, 400)

    player_mask = pygame.mask.from_surface(image_use)
    for p in pipes:
        p["x"] -= pipe_speed
        p["rect"].x = round(p["x"])
        screen.blit(p["image"], p["rect"])
        offset = (p["rect"].x - player.x, p["rect"].y - player.y)
        if player_mask.overlap(p["mask"], offset):
            print("hit")

    pipes = [p for p in pipes if p["rect"].right > 0]

    #Update screen
    pygame.display.flip()

    #60 FPS
    clock.tick(tick)

pygame.quit()


