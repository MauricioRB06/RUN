# R.U.N Project - File 5
# Pygame [ https://www.pygame.org/docs/ ]
# OS [ https://docs.python.org/3/library/os.html ]
# SYS [ https://docs.python.org/3/library/sys.html ]

from os.path import join
from sys import exit

import pygame
from pygame.mixer import music
from pygame.sprite import Group

from Directorys_Settings import SCREEN, FPS, CLOCK, Height, f_music, \
    sfxLowFuel, bgGameMap1, bgGameMap2, imgLowFuel, \
    bgArcadeGame
from Game_Class import Player, Enemy, PoliceSirenAnimation, Fuel, ScoreGoal, \
    Bonus, BloodAnimation
from Game_Functions import GamePause, PlayerCrash, PlayerBusted, GameOver, \
    ScorePrint

pygame.init()
pygame.mixer.init()


def GameLoop(vehicle_selected):

    fuel = Fuel()
    rails = [156, 233, 313, 390, 470, 546, 627, 703, 783, 861]

    player_group = Group()
    enemies_group = Group()
    score_goal = Group()
    fuel_item = Group()
    bonus_items = Group()
    police_siren_animation = Group()
    kill_bonus_animation = Group()

    player = Player(vehicle_selected)
    player_group.add(player)

    player_score = ScoreGoal()
    score_goal.add(player_score)

    police_siren_images = PoliceSirenAnimation()
    police_siren_animation.add(police_siren_images)

    new_bonus = Bonus()
    bonus_items.add(new_bonus)

    game = True
    music.load(join(f_music, 'Game_Music.ogg'))
    music.set_volume(0.5)
    music.play(loops=-1)
    sfxLowFuel.set_volume(0.05)
    score = 0
    remaining_fuel = 219
    mov_y = 0

    while game:

        CLOCK.tick(FPS)

        if not fuel_item:
            fuel_item.add(fuel)

        if not enemies_group:
            for i in rails:
                enemy_type = Enemy(i)
                enemies_group.add(enemy_type)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.set_volume(0.2)
                    GamePause()
                    pygame.mixer.music.set_volume(0.7)

        y_move = mov_y % bgGameMap1.get_rect().height
        SCREEN.blit(bgGameMap1, (0, (y_move - bgGameMap1.get_rect().height)))
        if y_move < Height:
            SCREEN.blit(bgGameMap1, (0, y_move))

        player_collision = pygame.sprite.spritecollide(player, enemies_group, False)

        if player_collision:
            sfxLowFuel.stop()
            PlayerCrash(bgGameMap1, (0, (y_move - bgGameMap1.get_rect().height) - 15),
                        bgGameMap2, (0, (y_move - bgGameMap2.get_rect().height) - 15),
                        player_group, enemies_group, police_siren_animation,
                        player.rect.x, player.rect.y)
            GameOver(0, score)
            game = False

        if remaining_fuel <= 0:
            music.stop()
            sfxLowFuel.stop()
            PlayerBusted(bgGameMap1, (0, (y_move - bgGameMap1.get_rect().height) - 15),
                         bgGameMap2, (0, (y_move - bgGameMap2.get_rect().height) - 15),
                         player_group, enemies_group, police_siren_animation)
            GameOver(1, score)
            game = False

        player_group.update()
        fuel_item.update()
        kill_bonus_animation.update()
        bonus_items.update()
        enemies_group.update()
        score_goal.update()
        police_siren_animation.update()

        recharge = pygame.sprite.spritecollide(player, fuel_item, False)
        if recharge:
            sfxLowFuel.stop()
            if vehicle_selected == 1:
                score += 50
            elif vehicle_selected == 2:
                score += 100
            elif vehicle_selected == 3:
                score += 200
            else:
                score += 300
            Fuel.recharge(fuel)
            if remaining_fuel <= 50:
                remaining_fuel += 50
            elif remaining_fuel <= 150:
                remaining_fuel += 25
            else:
                remaining_fuel += 219 - remaining_fuel

        win_score = pygame.sprite.spritecollide(player_score, enemies_group, False)
        if win_score:
            if vehicle_selected == 1:
                score += 1
            elif vehicle_selected == 2:
                score += 1
            elif vehicle_selected == 3:
                score += 2
            else:
                score += 2

        bonus_kill = pygame.sprite.spritecollide(player, bonus_items, False)
        if bonus_kill:
            kill = BloodAnimation(new_bonus.rect.x, new_bonus.rect.y)
            kill_bonus_animation.add(kill)
            sfxLowFuel.stop()
            bonus_type = new_bonus.kill_bonus()
            if bonus_type == 1:
                score += 200
            elif bonus_type == 2:
                score += 100
            else:
                score += 300

        player_group.draw(SCREEN)
        enemies_group.draw(SCREEN)
        fuel_item.draw(SCREEN)
        bonus_items.draw(SCREEN)
        kill_bonus_animation.draw(SCREEN)
        police_siren_animation.draw(SCREEN)
        score_goal.draw(SCREEN)

        y_move = mov_y % bgGameMap2.get_rect().height
        SCREEN.blit(bgGameMap2, (0, (y_move - bgGameMap2.get_rect().height)))

        if y_move < Height:
            SCREEN.blit(bgGameMap2, (0, y_move))

        SCREEN.blit(bgArcadeGame, (0, 0))

        if 1 < remaining_fuel <= 70:
            music.set_volume(0.3)
            sfxLowFuel.play()
            SCREEN.blit(imgLowFuel, (185, 150))
            pygame.draw.rect(SCREEN, (200, 100, 100), (418, 941, remaining_fuel, 15))
        elif 70 < remaining_fuel <= 149:
            music.set_volume(0.5)
            pygame.draw.rect(SCREEN, (252, 209, 42), (418, 941, remaining_fuel, 15))
        else:
            music.set_volume(0.5)
            pygame.draw.rect(SCREEN, (100, 200, 100), (418, 941, remaining_fuel, 15))

        remaining_fuel -= 0.06
        ScorePrint(str(score).zfill(10), 540, 900, (0, 0, 0), 20)
        mov_y += 15
        pygame.display.update()

    return score
