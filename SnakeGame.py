import pygame
import random
from time import sleep

# initialise
pygame.init()

# configurations 
fps = 22

width,height = 900,600

food_x = random.randint(20,width-20)
food_y = random.randint(20,height-20)

snake_size = 15
snake_x = 440
snake_y = 300
vel_x = 0
vel_y = 0

snake_list = []
snake_length = 1

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,35)

# functions
def scoreboard(text,colour,x,y):
    text = font.render(text,True,colour)
    screen.blit(text,(x,y))

def plot_snake(screen,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen,color,(x,y,snake_size,snake_size))


# defining colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

# game variables 
exit_game = False
game_over = False
score = 0

# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and vel_x != -5:
                vel_x = 5
                vel_y = 0
            if event.key == pygame.K_a and vel_x != 5:
                vel_x = -5
                vel_y = 0
            if event.key == pygame.K_w and vel_y != 5:
                vel_x = 0
                vel_y = -5
            if event.key == pygame.K_s and vel_y != -5:
                vel_x = 0
                vel_y = 5

    snake_x = snake_x + vel_x
    snake_y = snake_y + vel_y

    if snake_x <= 0:
        snake_x = width-snake_size
    if snake_x >= width:
        snake_x = 0
    if snake_y <= 0:
        snake_y = height-snake_size
    if snake_y >= height:
        snake_y = 0
    
    if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
        score = score + 1
        food_x = random.randint(20,width-20)
        if food_x in snake_list:
            food_x = random.randint(20,width-20)
        food_y = random.randint(20,height-20)
        if food_y in snake_list:
            food_y = random.randint(20,height-20)
        snake_length += 8

    screen.fill(white)
    scoreboard("Score: "+str(score),green,390,10)
    pygame.draw.rect(screen,red,[food_x,food_y,snake_size,snake_size])    

    head = [snake_x,snake_y]
    snake_list.append(head)

    if len(snake_list)>snake_length:
        del snake_list[0]

    if head in snake_list[:-1]:
        game_over = True

    if game_over:
        scoreboard("Game Over! ",red,380,300)
        pygame.display.update()
        sleep(3)
        exit_game = True

    plot_snake(screen,black,snake_list,snake_size)
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
quit()