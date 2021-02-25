# R.U.N Project - File 2
# Pygame [ https://www.pygame.org/docs/ ]
# OS [ https://docs.python.org/3/library/os.html ]
# TIME [ https://docs.python.org/3/library/time.html ]
# SYS [ https://docs.python.org/3/library/sys.html ]

from os.path import join
from sys import exit
from time import sleep

import pygame
from pygame import display
from pygame.font import Font
from pygame.image import load
from pygame.mixer import music

from Directorys_Settings import SCREEN, CLOCK, Width, f_music, f_gameOver, f_vfx,\
    sfxCrash, sfxBusted, game_folder

from Directorys_Settings import bgArcadePause, bgArcadeGameOver, bgArcadeLose,\
    imgPause, imgBusted, imgCrash, imgGameOverCrash, imgGameOverPolice, bgGameOver


def ScorePrint(score, x, y, color, size):
    score_font = Font(join(game_folder, '04B30.ttf'), size)
    surface = score_font.render(score, True, color)
    size_text = surface.get_rect()
    size_text.center = (x, y)
    SCREEN.blit(surface, size_text)


def HighScore():
    scores = open("High_Scores.user", "r")
    score_1 = scores.readline()
    score_2 = scores.readline()
    score_3 = scores.readline()
    scores.close()
    return score_1.strip(), score_2.strip(), score_3.strip()


def ScoreOrder():
    scores_order = []

    with open('High_Scores.user', 'r') as scores:
        scores_list = [score.strip() for score in scores]
    scores.close()

    for i in range(0, len(scores_list)):
        scores_order.append(int(scores_list[i]))

    scores_order.sort(reverse=True)

    with open('High_Scores.user', 'w') as scores:
        for line in range(0, len(scores_order)):
            scores.write("%s \n" % (scores_order[line]))
    scores.close()


def GamePause():
    game_pause = True
    while game_pause:
        CLOCK.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_pause = False
                    SCREEN.blit(imgPause, (0, 0))
        SCREEN.blit(bgArcadePause, (0, 0))
        display.update()


def PlayerCrash(background_game1, background_move1, background_game2, background_move2,
                player, enemies, siren, x, y):
    music.stop()
    crash = True
    coin_animation = 0
    sfxCrash.play()
    while crash:
        CLOCK.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        SCREEN.blit(background_game1, background_move1)
        player.draw(SCREEN)
        enemies.draw(SCREEN)
        SCREEN.blit(load(join(f_vfx, f'explosion_{coin_animation}.png'))
                    .convert_alpha(), (x - 30, y - 9))
        SCREEN.blit(background_game2, background_move2)
        siren.draw(SCREEN)
        SCREEN.blit(imgCrash, (0, 0))
        SCREEN.blit(bgArcadeGameOver, (0, 0))
        display.update()
        coin_animation += 1
        if coin_animation == 7:
            crash = False
    player.draw(SCREEN)
    enemies.draw(SCREEN)
    SCREEN.blit(load(join(f_vfx, 'explosion_3.png')).convert_alpha(), (x - 30, y - 9))
    SCREEN.blit(background_game2, background_move2)
    siren.draw(SCREEN)
    SCREEN.blit(imgCrash, (0, 0))
    SCREEN.blit(bgArcadeLose, (0, 0))
    display.update()
    sleep(1)


def PlayerBusted(background_game1, background_move1, background_game2, background_move2,
                 player, enemies, siren):
    music.stop()
    busted = True
    sfxBusted.play()
    while busted:
        CLOCK.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        SCREEN.blit(background_game1, background_move1)
        player.draw(SCREEN)
        enemies.draw(SCREEN)
        SCREEN.blit(background_game2, background_move2)
        siren.draw(SCREEN)
        SCREEN.blit(imgBusted, (0, 0))
        SCREEN.blit(bgArcadeLose, (0, 0))
        display.update()
        sleep(7)
        busted = False


def GameOver(game_event, score):
    game_over_animation = True
    game_event = game_event
    music.load(join(f_music, 'Game_Over_Music.ogg'))
    music.play(loops=-1)
    music.set_volume(0.7)
    police_animation = 1
    fire_smoke_animation = 1
    mov_x = 0
    while game_over_animation:
        CLOCK.tick(8)
        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                exit()
            if game_event.type == pygame.KEYDOWN:
                if game_event.key == pygame.K_SPACE:
                    game_over_animation = False

        x_move = mov_x % bgGameOver.get_rect().width
        SCREEN.blit(bgGameOver, ((x_move - bgGameOver.get_rect().width), 70))

        if x_move < Width:
            SCREEN.blit(bgGameOver, (x_move, 70))

        if game_event == 1:
            SCREEN.blit(imgGameOverPolice, (0, 0))
            SCREEN.blit(load(join(f_gameOver, f'PoliceCar_01_{fire_smoke_animation}.png'))
                        .convert_alpha(), (50, 460))
            SCREEN.blit(load(join(f_gameOver, f'PoliceCar_02_{fire_smoke_animation}.png'))
                        .convert_alpha(), (590, 450))
            SCREEN.blit(load(join(f_gameOver, f'Policeman_{police_animation}.png'))
                        .convert_alpha(), (475, 510))
            SCREEN.blit(load(join(f_gameOver, f'Men_{police_animation}.png'))
                        .convert_alpha(), (450, 535))
        else:
            SCREEN.blit(imgGameOverCrash, (0, 0))
            SCREEN.blit(load(join(f_vfx, f'Fire_01_{fire_smoke_animation}.png'))
                        .convert_alpha(), (580, 400))
            SCREEN.blit(load(join(f_vfx, f'Smoke_{fire_smoke_animation}.png'))
                        .convert_alpha(), (510, 450))
            SCREEN.blit(load(join(f_vfx, f'Fire_02_{police_animation}.png'))
                        .convert_alpha(), (415, 570))

        ScorePrint(str(score).zfill(10), 720, 180, (236, 219, 83), 30)
        SCREEN.blit(bgArcadeGameOver, (0, 0))
        police_animation += 1
        fire_smoke_animation += 1
        mov_x += 15
        if police_animation == 5:
            police_animation = 1
        if fire_smoke_animation == 9:
            fire_smoke_animation = 1
        display.update()
    SCREEN.fill((0, 0, 0))
