# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 													  #
# 				      R.U.N Project 	              #
# 													  #
#           Final Project Computer Programming        #
#                                                     #
#       National university of Colombia - 2020 II     #
#           Teacher: Juan Diego Escobar Mejia         #
#                                                     #
# 			     Language:  Python 3.9		     	  #
#                                                     #
#                     Programmers:                    #
# 													  #
#    Mauricio Rodriguez Becerra  - Eng. Mechatronic   #
#                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# R.U.N Project - File 1
# This file contains the root directories and files of the project, this reduces the
# lines of code that we will have to use later, by returning the calls to files and
# location paths a variable that we can use, The only resources that are not contained
# within this directory file are the images that we are going to modify at runtime to
# make animations.

# OS [ https://docs.python.org/3/library/os.html ]
# Pygame [ https://www.pygame.org/docs/ ]

from os.path import join, dirname
from pygame.mixer import Sound, init
from pygame.display import set_caption, set_icon, set_mode
from pygame.time import Clock
from pygame.image import load
from pygame.transform import scale

# ---------- Directory creation

game_folder = dirname(__file__)
images_folder = join(game_folder, 'Pixel_Art')
sounds_folder = join(game_folder, 'Sounds')
f_menu = join(images_folder, 'Menu')
f_backgrounds = join(images_folder, 'Backgrounds')
f_vfx = join(images_folder, 'VFX')
f_enemies = join(images_folder, 'Enemies')
f_items = join(images_folder, 'Items')
f_vehicles = join(images_folder, 'Vehicles')
f_music = join(sounds_folder, 'Music')
f_sfx = join(sounds_folder, 'SFX')
f_pause = join(f_menu, 'Pause')
f_gameOver = join(f_menu, 'Game_Over')
f_coin = join(f_menu, 'Insert_Coin')
f_load = join(f_menu, 'Load_Game')
f_howToPlay = join(f_menu, 'How_To_Play')
f_highScore = join(f_menu, 'High_Score')
f_credits = join(f_menu, 'Credits')
f_vehicleSelected = join(f_menu, 'Vehicle_Select')

# ---------- Base screen creation

CLOCK = Clock()
FPS = 60
Width, Height = 1000, 1000
SCREEN = set_mode((Width, Height))
set_caption('Racing UN')
set_icon(load(join(images_folder, 'icon.png')).convert_alpha())

# ---------- Assets creation - images

imgCursor = scale(load(join(f_menu, 'Cursor.png')).convert_alpha(), (50, 47))
bgGameOver = load(join(f_backgrounds, 'Game_Over.png')).convert_alpha()
bgMenu = load(join(f_backgrounds, 'Menu.png')).convert_alpha()
bgVehicleSelection = load(join(f_backgrounds, 'Bg_Vehicle.png')).convert_alpha()
bgLoading = load(join(f_backgrounds, 'Loading.png')).convert_alpha()
bgHighScores = load(join(f_backgrounds, 'High_Score.png')).convert_alpha()
bgHowToPlay = load(join(f_backgrounds, 'How_To_Play.png')).convert_alpha()
bgGameMap1 = load(join(f_backgrounds, 'Game_Map1_1.png')).convert_alpha()
bgGameMap2 = load(join(f_backgrounds, 'Game_Map1_2.png')).convert_alpha()
bgArcadeMenu = load(join(f_backgrounds, 'Arcade_Menu.png')).convert_alpha()
bgArcadeGame = load(join(f_backgrounds, 'Arcade_In_Game.png')).convert_alpha()
bgArcadePause = load(join(f_backgrounds, 'Arcade_pause.png')).convert_alpha()
bgArcadeGameOver = load(join(f_backgrounds, 'Bg_Game_Over.png')).convert_alpha()
bgArcadeLose = load(join(f_backgrounds, 'Arcade_Lose.png')).convert_alpha()
imgPause = load(join(f_pause, 'Image_pause.png')).convert_alpha()
imgLoad = load(join(f_load, 'loading.png')).convert_alpha()
imgCrash = load(join(f_gameOver, 'Crash.png')).convert_alpha()
imgBusted = load(join(f_gameOver, 'Busted.png')).convert_alpha()
imgGameOverPolice = load(join(f_gameOver, 'Your_Busted.png')).convert_alpha()
imgGameOverCrash = load(join(f_gameOver, 'Your_Crash.png')).convert_alpha()
imgLowFuel = load(join(f_items, 'Low_Fuel.png')).convert_alpha()
imgCars = load(join(f_vehicleSelected, 'Select_Car.png')).convert_alpha()
imgCredits = load(join(f_credits, 'Credits_Image.png')).convert_alpha()
imgHowToPlay = load(join(f_howToPlay, 'How_To_Play.png')).convert_alpha()
imgHighScore = load(join(f_highScore, 'Best_Scores.png')).convert_alpha()
imgBonus1 = load(join(f_items, 'Bonus_1.png')).convert_alpha()
imgBonus2 = load(join(f_items, 'Bonus_2.png')).convert_alpha()
imgBonus3 = load(join(f_items, 'Bonus_3.png')).convert_alpha()

# ---------- Assets creation - sounds

init()
sfxCrash = Sound(join(f_sfx, 'Crash.ogg'))
sfxBusted = Sound(join(f_sfx, 'Busted.ogg'))
sfxLowFuel = Sound(join(f_sfx, 'Low_Gasoline.ogg'))
sfxButtonClick = Sound(join(f_sfx, 'Button_Click.ogg'))
sfxBloodPorky = Sound(join(f_sfx, 'Porky.ogg'))
sfxBloodOldWoman = Sound(join(f_sfx, 'Gloria.ogg'))
sfxBloodPolice = Sound(join(f_sfx, 'Police.ogg'))
sfxCat = Sound(join(f_sfx, 'Cat.ogg'))
sfxPowerUp = Sound(join(f_sfx, 'Fuel_PowerUp.ogg'))
