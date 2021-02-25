# R.U.N Project - File 3
# Pygame [ https://www.pygame.org/docs/ ]
# OS [ https://docs.python.org/3/library/os.html ]
# RANDOM [ https://docs.python.org/3/library/random.html ]

from os.path import join
from random import choice, randint

import pygame
from pygame.image import load
from pygame.sprite import Sprite

from Directorys_Settings import Height, f_vehicles, f_enemies, f_items, f_vfx,\
     sfxPowerUp, sfxBloodPolice

from Directorys_Settings import sfxBloodPorky, sfxBloodOldWoman, imgBonus1,\
     imgBonus2, imgBonus3


class Player(Sprite):

    def __init__(self, vehicle_select):
        self.level = vehicle_select
        self.speed = 0
        super().__init__()
        self.image = load(join(f_vehicles, f'Vehicle_0{vehicle_select}.png'))\
            .convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (1024 // 2, 690)

    def update(self):

        self.speed = 0
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_LEFT]:
            self.speed = -(8 - self.level)
        if pressed_key[pygame.K_RIGHT]:
            self.speed = 8 - self.level

        self.rect.x += self.speed

        if self.rect.left < 119:
            self.rect.left = 119
        if self.rect.right > 895:
            self.rect.right = 895


class Enemy(Sprite):

    enemies_images = []
    for num in range(0, 16):
        enemy = load(join(f_enemies, f'Enemy_{num}.png')).convert_alpha()
        enemies_images.append(enemy)

    def __init__(self, number_rail):
        super().__init__()
        self.image = choice(self.enemies_images)
        self.rect = self.image.get_rect()
        self.rect.center = (randint((number_rail - 6), (number_rail + 6)),
                            -(randint(200, 550)))
        self.speed = randint(6, 10)
        self.new_pos = number_rail

    def update(self):

        self.rect.y += self.speed
        if self.rect.top > Height:
            self.speed = randint(6, 10)
            self.image = choice(self.enemies_images)
            self.rect = self.image.get_rect()
            self.rect.center = (randint((self.new_pos - 6), (self.new_pos + 6)),
                                -(randint(200, 550)))


class Fuel(Sprite):

    fuel_animation = []
    for num in range(0, 6):
        fuel_image = pygame.image.load(join(f_items, f'Fuel_{num}.png')).convert_alpha()
        fuel_animation.append(fuel_image)

    def __init__(self):
        super().__init__()
        self.image = choice(self.fuel_animation)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(145, 876), -3000)
        self.speed = 8

    def update(self):
        self.rect.y += self.speed
        self.image = choice(self.fuel_animation)
        if self.rect.top > (Height + 3000):
            self.rect.center = (randint(145, 876), -3000)

    def recharge(self):
        sfxPowerUp.play()
        self.rect.center = (randint(145, 876), -4500)


class ScoreGoal(Sprite):

    def __init__(self):
        super().__init__()
        self.image = load(join(f_enemies, 'Score_goal.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (500, 800)

    def update(self):
        self.rect.center = (500, 800)


class Bonus(Sprite):

    def __init__(self):
        super().__init__()
        self.option = randint(1, 3)
        if self.option == 1:
            self.image = imgBonus1
        elif self.option == 2:
            self.image = imgBonus2
        else:
            self.image = imgBonus3
        self.rect = self.image.get_rect()
        self.rect.center = (randint(145, 876), -4000)
        self.speed = 8

    def randomise(self):
        self.option = randint(1, 3)
        if self.option == 1:
            self.image = imgBonus1
            self.rect = self.image.get_rect()
        elif self.option == 2:
            self.image = imgBonus2
            self.rect = self.image.get_rect()
        else:
            self.image = imgBonus3
            self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > (Height + 4000):
            self.randomise()
            self.rect.center = (randint(145, 876), -4000)

    def kill_bonus(self):
        if self.option == 1:
            sfxBloodPorky.play()
        elif self.option == 2:
            sfxBloodOldWoman.play()
        else:
            sfxBloodPolice.play()
        bonus_kill = self.option
        self.randomise()
        self.rect.center = (randint(145, 876), -8000)
        return bonus_kill


class PoliceSirenAnimation(Sprite):

    sirens = []
    for num in range(1, 7):
        siren_image = load(join(f_vfx, f'siren_{num}.png')).convert_alpha()
        sirens.append(siren_image)

    def __init__(self):
        super().__init__()
        self.image = choice(self.sirens)
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)

    def update(self):
        self.image = choice(self.sirens)


class BloodAnimation(Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.center = (500, 500)
        self.kill_anim = []
        for num in range(1, 6):
            blood = load(join(f_vfx, f'Blood_{num}.png')).convert_alpha()
            blood = pygame.transform.scale(blood, (100, 100))
            self.kill_anim.append(blood)
        self.index = 0
        self.image = self.kill_anim[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x + 50, y + 100]
        self.counter = 0

    def update(self):

        blood_speed = 6
        self.counter += 1
        self.center = (500, 500)
        if self.counter >= blood_speed and self.index < len(
                self.kill_anim) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.kill_anim[self.index]

        if self.index >= len(
                self.kill_anim) - 1 and self.counter >= blood_speed:
            self.kill()
