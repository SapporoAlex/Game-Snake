import pygame
import random
import pygame.mixer

pygame.init()
pygame.mixer.init()
# pygame.mixer.set_num_channels(2)
chomp_sfx = pygame.mixer.Sound("assets/chomp.mp3")
boing_sfx = pygame.mixer.Sound("assets/boing.mp3")
pygame.mixer.music.load("assets/music0.mp3")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
old_phone1 = (169, 179, 169)
old_phone2 = (159, 179, 149)
old_phone3 = (149, 179, 129)
old_phone4 = (139, 179, 109)
old_phone5 = (129, 179, 89)
old_phone6 = (119, 179, 69)
old_phone7 = (109, 179, 49)
old_phone8 = (99, 179, 29)
old_phone9 = (0, 0, 0)
dis_width = 600
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15

font_style = pygame.font.SysFont('Lucida Console', 15)

high_score_file = "highscore.txt"
try:
    with open(high_score_file, "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0


def update_high_score(new_score):
    global high_score
    if new_score > high_score:
        high_score = new_score
        with open(high_score_file, "w") as file:
            file.write(str(high_score))


def player_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def game_loop():

    def display_score():
        score_text = font_style.render(f"Score: {score}   Hi-Score: {high_score}", 1, score_text_colour)
        dis.blit(score_text, (10, 10))

    music_playing = False
    game_over = False
    game_close = False
    score_text_colour = white
    x1 = dis_width / 2
    y1 = dis_height / 2
    music_level = 0
    x1_change = 0
    y1_change = 0
    current_level_colour = old_phone1
    snake_List = []
    Length_of_snake = 1
    score = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / float(snake_block)) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / float(snake_block)) * snake_block

    while not game_over:

        while game_close:
            music_level = 0
            pygame.mixer.music.unload()
            pygame.mixer.music.load("assets/music0.mp3")
            dis.fill(white)
            message("You Lost! Press Q to Quit or C to Play Again", black)
            display_score()
            score_text_colour = black
            player_snake(snake_block, snake_List)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

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
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            boing_sfx.play()
            game_close = True

        x1 += x1_change
        y1 += y1_change

        if not music_playing:
            pygame.mixer.music.play(loops=-1)
            music_playing = True

        if score < 10:
            music_level = 0
            current_level_colour = old_phone1
        elif score < 20 and music_level == 1.5:
            pass
        elif score < 20:
            music_level = 1
            current_level_colour = old_phone2
            if music_level == 1:
                music_level = 1.5
                pygame.mixer.music.load("assets/music1.mp3")
                pygame.mixer.music.play(loops=-1)
        elif score < 30 and music_level == 2.5:
            pass
        elif score < 30:
            music_level = 2
            current_level_colour = old_phone3
            if music_level == 2:
                music_level = 2.5
                pygame.mixer.music.load("assets/music2.mp3")
                pygame.mixer.music.play(loops=-1)
        elif score < 40 and music_level == 3.5:
            pass
        elif score < 40:
            music_level = 3
            current_level_colour = old_phone4
            if music_level == 3:
                music_level = 3.5
                pygame.mixer.music.load("assets/music3.mp3")
                pygame.mixer.music.play(loops=-1)
        elif score < 40 and music_level == 4.5:
            pass
        elif score < 40:
            music_level = 4
            current_level_colour = old_phone5
            if music_level == 4:
                music_level = 4.5
                pygame.mixer.music.load("assets/music4.mp3")
                pygame.mixer.music.play(loops=-1)
        elif score < 50 and music_level == 5.5:
            pass
        elif score < 50:
            music_level = 5
            current_level_colour = old_phone6
            if music_level == 5:
                music_level = 5.5
                pygame.mixer.music.load("assets/music5.mp3")
                pygame.mixer.music.play(loops=-1)
        elif score < 60 and music_level == 6.5:
            pass
        elif score < 60:
            music_level = 6
            current_level_colour = old_phone7
            if music_level == 6:
                music_level = 6.5
                pygame.mixer.music.load("assets/music6.mp3")
                pygame.mixer.music.play(loops=-1)
        elif score < 70 and music_level == 7.5:
            pass
        elif score < 70:
            music_level = 7
            current_level_colour = old_phone8
            if music_level == 7:
                music_level = 7.5
                pygame.mixer.music.load("assets/music7.mp3")
                pygame.mixer.music.play(loops=-1)
        elif score < 80 and music_level == 8.5:
            pass
        elif score < 80:
            music_level = 8
            current_level_colour = old_phone9
            if music_level == 8:
                music_level = 8.5
                pygame.mixer.music.load("assets/music8.mp3")
                pygame.mixer.music.play(loops=-1)

        dis.fill(current_level_colour)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                boing_sfx.play()
                game_close = True

        player_snake(snake_block, snake_List)
        display_score()
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / float(snake_block)) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / float(snake_block)) * snake_block
            chomp_sfx.play()
            score += 1
            Length_of_snake += 1
            update_high_score(score)

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
