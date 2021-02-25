# R.U.N Project - File 4
# Pygame [ https://www.pygame.org/docs/ ]
# OS [ https://docs.python.org/3/library/os.html ]
# TIME [ https://docs.python.org/3/library/time.html ]

from os.path import join
from time import sleep

import pygame
from pygame import Rect, mouse, display, MOUSEBUTTONDOWN
from pygame.font import Font
from pygame.image import load
from pygame.mixer import music
from pygame.transform import scale

import Game_Loop
from Directorys_Settings import SCREEN, CLOCK, Width, Height, f_music, f_coin, \
    sfxButtonClick, imgCars, bgArcadeMenu, imgCursor, imgCredits, f_backgrounds, \
    sfxCat, sfxBloodPolice, sfxPowerUp, game_folder

from Directorys_Settings import bgMenu, bgLoading, bgArcadeGame, imgLoad, \
    bgVehicleSelection, bgHighScores, bgHowToPlay, imgHowToPlay, sfxBloodOldWoman, \
    sfxBloodPorky, imgHighScore, f_vfx

from Game_Functions import ScorePrint, ScoreOrder, HighScore

pygame.init()
pygame.mixer.init()
menuFont = Font(join(game_folder, '04B30.ttf'), 60)
carFont = Font(join(game_folder, '04B30.ttf'), 35)
mouse.set_visible(False)
game_on = True
sfxButtonClick.set_volume(0.5)


def ButtonsPrint(button, name, font):
    if button.collidepoint(mouse.get_pos()):
        text = font.render(name, True, (235, 47, 47))
        SCREEN.blit(text, (button.x + (button.width + 10 - text.get_width()) / 2,
                           button.y + (button.height - 3 - text.get_height()) / 2))
    else:
        text = font.render(name.lower(), True, (245, 245, 245))
        SCREEN.blit(text, (button.x + (button.width + 10 - text.get_width()) / 2,
                           button.y + (button.height - 3 - text.get_height()) / 2))


def MainMenu():
    button_play = Rect((Width // 4), 200, 192, 42)
    button_high_score = Rect((Width // 4), 305, 470, 42)
    button_how_to_play = Rect((Width // 4), 410, 540, 42)
    button_credits = Rect((Width // 4), 515, 320, 42)
    button_exit = Rect((Width // 4), 620, 175, 42)
    coin_animation = 1
    coin_animation_control = 0
    x_mov = 0
    music.load(join(f_music, 'Menu_Music.ogg'))
    music.set_volume(0.15)
    music.play(loops=-1)

    while game_on:
        CLOCK.tick(Game_Loop.FPS)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_play.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    selection = VehicleSelectMenu()
                    if selection != 0:
                        sleep(1)
                        LoadGameScreen()
                        final_score = Game_Loop.GameLoop(selection)
                        LoadGameScreen()
                        music.load(join(f_music, 'Menu_Music.ogg'))
                        music.set_volume(0.15)
                        music.play(loops=-1)
                        save = open('High_Scores.user', 'a')
                        save.write(str(final_score) + '\n')
                        save.close()
                if button_high_score.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    HighScoreMenu()
                if button_how_to_play.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    HowToPlayMenu()
                if button_credits.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    music.stop()
                    CreditsMenu()
                    music.load(join(f_music, 'Menu_Music.ogg'))
                    music.set_volume(0.15)
                    music.play(loops=-1)
                if button_exit.collidepoint(
                        mouse.get_pos()):
                    sfxButtonClick.play()
                    sleep(1)
                    exit()

        x_move = x_mov % bgMenu.get_rect().width
        SCREEN.blit(bgMenu, ((x_move - bgMenu.get_rect().width), 70))
        if x_move < Width:
            SCREEN.blit(bgMenu, (x_move, 70))

        ButtonsPrint(button_play, 'PLAY', menuFont)
        ButtonsPrint(button_high_score, 'HIGH SCORE', menuFont)
        ButtonsPrint(button_how_to_play, 'HOW TO PLAY', menuFont)
        ButtonsPrint(button_credits, 'CREDITS', menuFont)
        ButtonsPrint(button_exit, 'EXIT', menuFont)

        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        SCREEN.blit(bgArcadeMenu, (0, 0))
        SCREEN.blit(scale(load(join(f_coin, f'Coin_{coin_animation}.png'))
                          .convert_alpha(), (220, 150)), (370, 855))

        x_mov -= 5
        coin_animation_control += 0.5

        if coin_animation_control % 6 == 0:
            coin_animation += 1
        if coin_animation > 6:
            coin_animation = 1
            coin_animation_control = 0

        display.update()


def LoadGameScreen():
    music.stop()
    load_bar = 0
    loading = True

    while loading:
        CLOCK.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        SCREEN.blit(bgLoading, (-240, 0))
        SCREEN.blit(imgLoad, (0, 0))
        pygame.draw.rect(SCREEN, (35, 100, 198), (185, 552, load_bar, 36))
        SCREEN.blit(bgArcadeGame, (0, 0))
        load_bar += 2
        display.update()
        if load_bar >= 632:
            loading = False
    sleep(2)


def VehicleSelectMenu():
    selection = True
    vehicle = 0
    coin_animation = 1
    coin_animation_control = 0
    x_mov = 0
    button_back = Rect(400, 690, 192, 42)
    button_car1 = Rect(100, 600, 170, 30)
    button_car2 = Rect(310, 600, 170, 30)
    button_car3 = Rect(520, 600, 170, 30)
    button_car4 = Rect(730, 600, 170, 30)

    while selection:
        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    selection = False
                if button_car1.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    vehicle = 1
                    selection = False
                if button_car2.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    vehicle = 2
                    selection = False
                if button_car3.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    vehicle = 3
                    selection = False
                if button_car4.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    vehicle = 4
                    selection = False

        x_move = x_mov % bgVehicleSelection.get_rect().width
        SCREEN.blit(bgVehicleSelection,
                    ((x_move - bgVehicleSelection.get_rect().width), 72))
        if x_move < Width:
            SCREEN.blit(bgVehicleSelection, (x_move, 72))
        SCREEN.blit(imgCars, (0, 0))
        ButtonsPrint(button_back, 'BACK', menuFont)
        ButtonsPrint(button_car1, 'SELECT', carFont)
        ButtonsPrint(button_car2, 'SELECT', carFont)
        ButtonsPrint(button_car3, 'SELECT', carFont)
        ButtonsPrint(button_car4, 'SELECT', carFont)
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        SCREEN.blit(bgArcadeMenu, (0, 0))
        SCREEN.blit(scale(load(join(f_coin, f'Coin_{coin_animation}.png'))
                          .convert_alpha(), (220, 150)), (370, 855))

        x_mov -= 5
        coin_animation_control += 1

        if coin_animation_control % 6 == 0:
            coin_animation += 1
        if coin_animation > 6:
            coin_animation = 1
            coin_animation_control = 0
        display.update()
    return vehicle


def HighScoreMenu():
    scores_file = open('High_Scores.user', 'a')
    ScoreOrder()
    score_1, score_2, score_3 = HighScore()
    check_high_scores = True
    x_mov = 0
    coin_animation = 1
    coin_animation_control = 0
    bongo_cat_animation = 1
    bongo_cat_animation_control = 0
    button_back = Rect(400, 690, 192, 42)
    button_cat_sound = Rect(710, 160, 100, 100)

    while check_high_scores:
        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    check_high_scores = False
                if button_cat_sound.collidepoint(mouse.get_pos()):
                    sfxCat.play()

        ButtonsPrint(button_cat_sound, ':3', menuFont)
        x_move = x_mov % bgHighScores.get_rect().width
        SCREEN.blit(bgHighScores, ((x_move - bgHighScores.get_rect().width), 70))
        if x_move < Width:
            SCREEN.blit(bgHighScores, (x_move, 70))

        SCREEN.blit(imgHighScore, (0, 0))
        ButtonsPrint(button_back, 'BACK', menuFont)
        ScorePrint(score_1.zfill(10), 650, 379, (0, 0, 0), 50)
        ScorePrint(score_1.zfill(10), 650, 375, (255, 255, 255), 50)
        ScorePrint(score_2.zfill(10), 650, 484, (0, 0, 0), 50)
        ScorePrint(score_2.zfill(10), 650, 480, (255, 255, 255), 50)
        ScorePrint(score_3.zfill(10), 650, 584, (0, 0, 0), 50)
        ScorePrint(score_3.zfill(10), 650, 580, (255, 255, 255), 50)
        SCREEN.blit(scale(load(join(f_vfx, f'Bongo_Cat_{bongo_cat_animation}.png'))
                          .convert_alpha(), (198, 198)), (650, 110))
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        SCREEN.blit(bgArcadeMenu, (0, 0))
        SCREEN.blit(scale(load(join(f_coin, f'Coin_{coin_animation}.png'))
                          .convert_alpha(), (220, 150)), (370, 855))

        x_mov -= 5
        coin_animation_control += 0.5
        bongo_cat_animation_control += 2

        if bongo_cat_animation_control % 10 == 0:
            bongo_cat_animation += 1
        if bongo_cat_animation == 21:
            bongo_cat_animation = 1

        if coin_animation_control % 6 == 0:
            coin_animation += 1
        if coin_animation > 6:
            coin_animation = 1
            coin_animation_control = 0
        display.update()
    scores_file.close()


def HowToPlayMenu():
    check_how_to_play = True
    coin_animation = 1
    coin_animation_control = 0
    x_mov = 0
    button_back = Rect(630, 670, 192, 42)
    bonus_1_sound = Rect(210, 580, 50, 70)
    bonus_2_sound = Rect(330, 580, 50, 70)
    bonus_3_sound = Rect(460, 580, 50, 70)
    fuel_sound = Rect(330, 440, 50, 50)

    while check_how_to_play:
        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    check_how_to_play = False
                if bonus_1_sound.collidepoint(mouse.get_pos()):
                    sfxBloodPorky.play()
                if bonus_2_sound.collidepoint(mouse.get_pos()):
                    sfxBloodOldWoman.play()
                if bonus_3_sound.collidepoint(mouse.get_pos()):
                    sfxBloodPolice.play()
                if fuel_sound.collidepoint(mouse.get_pos()):
                    sfxPowerUp.play()

        ButtonsPrint(bonus_1_sound, '1', menuFont)
        ButtonsPrint(bonus_2_sound, '2', menuFont)
        ButtonsPrint(bonus_3_sound, '3', menuFont)
        ButtonsPrint(fuel_sound, 'F', menuFont)
        x_move = x_mov % bgHowToPlay.get_rect().width
        SCREEN.blit(bgHowToPlay, ((x_move - bgHowToPlay.get_rect().width), 70))
        if x_move < Width:
            SCREEN.blit(bgHowToPlay, (x_move, 70))
        SCREEN.blit(imgHowToPlay, (0, 0))
        ButtonsPrint(button_back, 'BACK', menuFont)
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        SCREEN.blit(bgArcadeMenu, (0, 0))
        SCREEN.blit(scale(load(join(f_coin, f'Coin_{coin_animation}.png'))
                          .convert_alpha(), (220, 150)), (370, 855))

        x_mov -= 5
        coin_animation_control += 0.5

        if coin_animation_control % 6 == 0:
            coin_animation += 1
        if coin_animation > 6:
            coin_animation = 1
            coin_animation_control = 0
        display.update()


def CreditsMenu():
    music.load(join(f_music, 'Credits_Music.ogg'))
    music.set_volume(0.5)
    music.play(loops=-1)
    check_credits_menu = True
    coin_animation = 1
    coin_animation_control = 0
    num_image = 1
    y_mov = 0
    background_animation_control = 0
    button_back = Rect(400, 690, 192, 42)
    button_cat_sound = Rect(850, 500, 100, 100)
    while check_credits_menu:

        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if button_back.collidepoint(mouse.get_pos()):
                    sfxButtonClick.play()
                    check_credits_menu = False
                if button_cat_sound.collidepoint(mouse.get_pos()):
                    sfxCat.play()

        ButtonsPrint(button_cat_sound, ':3', menuFont)
        SCREEN.blit(scale(load(join(f_backgrounds, f'Credits_{num_image}.png'))
                          .convert_alpha(), (1040, 701)), (0, 80))
        y_move = y_mov % imgCredits.get_rect().height
        SCREEN.blit(imgCredits, (0, (y_move - imgCredits.get_rect().height)))
        if y_move < Height:
            SCREEN.blit(imgCredits, (0, y_move))
        SCREEN.blit(scale(load(join(f_backgrounds, f'CreditsT_{num_image}.png'))
                          .convert_alpha(), (1040, 701)), (0, 80))
        ButtonsPrint(button_back, 'BACK', menuFont)
        SCREEN.blit(imgCursor, (mouse_pos[0], mouse_pos[1]))
        SCREEN.blit(bgArcadeMenu, (0, 0))
        SCREEN.blit(scale(load(join(f_coin, f'Coin_{coin_animation}.png'))
                          .convert_alpha(), (220, 150)), (370, 855))

        y_mov -= 0.75
        coin_animation_control += 0.5
        background_animation_control += 1

        if background_animation_control % 8 == 0:
            num_image += 1
        if num_image == 9:
            num_image = 1

        if coin_animation_control % 6 == 0:
            coin_animation += 1
        if coin_animation > 6:
            coin_animation = 1
            coin_animation_control = 0
        display.update()
    music.stop()


MainMenu()
