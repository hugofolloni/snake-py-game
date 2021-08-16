import pygame
import random

pygame.init()

black = (0,0,0)
red = (213,50,89)
green = (12, 89, 0)
blue = (50,123,213)

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SnakeGame @hugofolloni')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("sans-serif", 25)
score_font = pygame.font.SysFont("sans-serif", 35)

def Score(score):
    value = score_font.render("Pontuação: " + str(score), True, blue)
    display.blit(value, [0, 0])

def Snake(snake_block, snake_list):
    for x in snake_list:
        	pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    messageWrite = font_style.render(msg, True, color)
    display.blit(messageWrite, [display_width / 6 - 25, display_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10 ) * 10
    foody = round(random.randrange(0, display_height - snake_block) / 10) * 10


    while not game_over:

        while game_close == True:
            display.fill(black)
            message("Você perdeu! Clique C para jogar de novo e Q para sair", red)
            Score("DERROTA")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change
        
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True
        
        Snake(snake_block, snake_list)
        Score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
