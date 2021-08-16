import pygame
import random

pygame.init() #Inicia o jogo


black = (0,0,0) #Seta as cores usadas
red = (213,50,89)
green = (12, 89, 0)
blue = (50,123,213)

display_width = 600
display_height = 400

display = pygame.display.set_mode((display_width, display_height)) #Seta o tamanho da tela
pygame.display.set_caption('SnakeGame @hugofolloni') #Nome da janela

clock = pygame.time.Clock()

snake_block = 10 #tamanho dos blocos
snake_speed = 15  #velocidade da cobra

font_style = pygame.font.SysFont("sans-serif", 25) #fontes usadas
score_font = pygame.font.SysFont("sans-serif", 35)

def Score(score): #define a funçõo que se encarregará de mostrar a pontuação
    value = score_font.render("Pontuação: " + str(score), True, blue)
    display.blit(value, [0, 0])

def Snake(snake_block, snake_list): #define a função que irá desenhar a cobra no jogo
    for x in snake_list:
        	pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color): #define a função que printará a mensagem pós jogo
    messageWrite = font_style.render(msg, True, color)
    display.blit(messageWrite, [display_width / 6 - 25, display_height / 3])

def gameLoop(): #inicia o loop do jogo
    game_over = False #o jogo nao está fechado e nem na tela de fechamento
    game_close = False

    x1 = display_width / 2 #posição inical da cobra
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = [] #define o tamanho da cobra
    length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10 ) * 10 #define a posição do primeiro alimento
    foody = round(random.randrange(0, display_height - snake_block) / 10) * 10


    while not game_over:

        while game_close == True: #se o jogo estiver na tela de fechamento
            display.fill(black)
            message("Você perdeu! Clique C para jogar de novo e Q para sair", red)
            Score("DERROTA")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN: #define as teclas para fechar o jogo
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): #andar com a cobra
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

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0: #definir os limites da área da cobra
            game_close = True


        x1 += x1_change
        y1 += y1_change #mudar a posição da cobra com base no ultimo movimento
        
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block]) #pintar a cobra no cenário
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]: #fecha o jogo caso a cobra bata em si mesma
            if x == snake_Head:
                game_close = True
        
        Snake(snake_block, snake_list)
        Score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0 #define a proxima comida
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1 #aumenta o tamanho da cobra

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()