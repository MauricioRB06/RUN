# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 													  #
# 				    Proyecto R.U.N	                  #
# 													  #
#	   Proyecto Final Pogramacion de Computadores     #
#													  #
#	   Universidad Nacional de Colombia - 2020 II     #
#	       Docente: Juan Diego Escobar Mejia          #
#	                      						      #
# 			       Lenguaje:  Python		     	  #
#	                      						      #
#	                 Programadores:   			      #
# 													  #
#	 Mauricio Rodriguez Becerra  - Ing. Mecatronica   #
#	 Laura Alejandra Paez Daza   - Ing. Mecatronica   #
#	 Juan Esteban Flechas Rincon - Ing. Electronica   #
#	 Alejandro Mendivelso Torres - Ing. Mecatronica   #
#												      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Pygame [ https://www.pygame.org/docs/ ]
# OS [ https://docs.python.org/3/library/os.html ]
# TIME [ https://docs.python.org/3/library/time.html ]

import pygame
from pygame import Rect, draw, mouse, display, MOUSEBUTTONDOWN
from pygame.image import load
from pygame.mixer import Sound, music
from pygame.transform import scale
from pygame.font import Font
from os.path import join
from time import sleep
from random import randint
from Directorys_Settings import SCREEN, CLOCK, FPS, W, H, f_music, f_coin, sfx_button_click, img_cars, arcade_menu, img_cursor, img_credits, f_backgrounds, sfx_perseo, sfx_blood_tombos, sfx_powerup
from Directorys_Settings import background_menu, background_load, arcade_game,img_load, background_car, background_h_s,background_ht_play, img_htp, sfx_blood_oldwoman, sfx_blood_porky, img_hs, f_vfx
import Game_Loop  # Importamos el módulo [ Game_Loop ]

# ----------------------------------------- Inicializar Pygame y Pygame Mixer ------------------------------------------------------------------------------------
pygame.init()
pygame.mixer.init()
menu_font = Font('04B30.ttf', 60)
car_font = Font('04B30.ttf', 35)
mouse.set_visible(0) # El metodo .set_visible() nos permite esconder el cursor de windows dentro de la ventana 0 = False / 1 = True
game_on = True

# --------------------------- Funciones = cargar juego/ seleccionar auto / puntuacion mas alta / como jugar / creditos / menu principal / imprimir botones -------

def print_buttons(button,name,font):  # Funcion para imprimir en pantalla los botones
    if button.collidepoint(mouse.get_pos()):           # si el mouse esta encima del boton
        text = font.render(name,True,(235,47,47)) # ponemos la letra de color rojo y mayuscula
        SCREEN.blit(text,(button.x + (button.width + 10 - text.get_width())/2,  # pintamos el texto en el centro del recuadro del boton
                      button.y + (button.height - 3 - text.get_height())/2 )) 
    else:                                                     # si el mouse no esta encima del boton
        text = font.render(name.lower(),True,(245,245,245))   # ponemos la letra de color blanco y minuscula
        SCREEN.blit(text,(button.x + (button.width + 10 - text.get_width())/2, 
                      button.y + (button.height - 3 - text.get_height())/2 )) # pintamos el texto en el centro del recuadro del boton

def main_menu():  # Funcion del menu principal

    button_play = Rect((W//4),200,192,42)     # Creamos un rectangulo ingresando la posicion (x,y) y luego el tamaño (ancho,alto) que simulara un boton
    button_hs = Rect((W//4),305,470,42)
    button_htp = Rect((W//4),410,540,42)
    button_credits = Rect((W//4),515,320,42)
    button_exit = Rect((W//4),620,175,42)
    coin = 1                                  # variable para animar el insert_coin
    x_mov = 0
    fps_control = 0                           # variable para controlar la velocidad de la animacion insert_coin
    music.load(join(f_music,'Menu_Music.ogg'))
    music.set_volume(0.3)
    music.play(loops=-1)

    while game_on:
        CLOCK.tick(Game_Loop.FPS)
        mouse_pos = mouse.get_pos() # El metodo .get_pos() nos devuelve una tupla con la posicion (x,y) del mouse en la pantalla
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # si el evento es de tipo presionar boton de mouse procedemos a revisar
                if button_play.collidepoint(mouse.get_pos()):        # el metodo .collidepoint() nos permite saber si un punto (x,y) en este caso la posicion del mouse
                    sfx_button_click.play()                          # colisiono con el rectangulo que representa al boton play en este caso y si es asi, desencadena el if
                    select = vehicle_select()
                    if select != 0:
                        sleep(1)
                        load_game()
                        result = Game_Loop.game_loop(select)
                        load_game()
                        music.load(join(f_music,'Menu_Music.ogg'))
                        music.set_volume(0.3)
                        music.play(loops=-1)
                        print(result)# print de prueba 
                if button_hs.collidepoint(mouse.get_pos()):          # revisa si el click colisiono con el boton high score
                    sfx_button_click.play()
                    high_score()                                     # llamamos a la funcion con el menu High Score                     
                if button_htp.collidepoint(mouse.get_pos()):         # revisa si el click colisiono con el boton
                    sfx_button_click.play()
                    how_to_play()                                    # llamamos a la funcion con el menu How To Play
                if button_credits.collidepoint(mouse.get_pos()):     # revisa si el click colisiono con el boton
                    sfx_button_click.play()
                    music.stop()
                    credits()
                    music.load(join(f_music,'Menu_Music.ogg'))
                    music.play(loops=-1)                                        # llamamos a la funcion con el menu Credits
                if button_exit.collidepoint(mouse.get_pos()):        # revisa si el click colisiono con el boton salir y cierra el sistema
                    sfx_button_click.play()
                    sleep(1)
                    exit()

        x_move = x_mov % background_menu.get_rect().width
        SCREEN.blit(background_menu,( (x_move - background_menu.get_rect().width),70 ))
        if x_move < W:
            SCREEN.blit(background_menu,(x_move,70))

        print_buttons(button_play,'PLAY',menu_font)         # Llamamos a la función print_buttons y le damos de parametro el rectangulo del boton correspondiente, y el texto que tendra el boton
        print_buttons(button_hs,'HIGH SCORE',menu_font)
        print_buttons(button_htp,'HOW TO PLAY',menu_font)
        print_buttons(button_credits,'CREDITS',menu_font)
        print_buttons(button_exit,'EXIT',menu_font)

        SCREEN.blit(img_cursor,(mouse_pos[0],mouse_pos[1])) # Despues de que se creen las imagenes y justo abajo de la imagen del arcade, creamos la iamgen de nuestro cursor personalizado
        SCREEN.blit(arcade_menu,(0,0))
        SCREEN.blit(scale(load(join(f_coin,f'Coin_{coin}.png')).convert_alpha(),(220,150)),(370,855))

        x_mov -= 5
        fps_control += 0.5

        if fps_control % 6 == 0:
            coin += 1
        if coin > 6:
            coin = 1
            fps_control = 0

        display.update()

def load_game():  # Funcion para mostrar animacion de carga del juego
    music.stop()
    load_bar = 0
    load = True
    while load:
        CLOCK.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()

        SCREEN.blit(background_load,(-240,0))
        SCREEN.blit(img_load,(0,0))
        pygame.draw.rect(SCREEN,(35,100,198),(185, 552, load_bar, 36))        
        SCREEN.blit(arcade_game,(0,0))   
        load_bar += 2
        display.update()
        if load_bar >= 632:
            load = False
    sleep(2)					  

def vehicle_select(): # Funcion para mostrar pantalla de selccion de vehiculo
    select = True
    vechicle = 0
    coin = 1                                  
    x_mov = 0
    fps_control = 0 
    button_back = Rect(400,690,192,42)
    button_car1 = Rect(80,600,170,30) 
    button_car2 = Rect(290,600,170,30) 
    button_car3 = Rect(510,600,170,30) 
    button_car4 = Rect(720,600,170,30)  
    while select:
        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  
                if button_back.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    select = False
                if button_car1.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    vechicle = 1
                    select = False
                if button_car2.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    vechicle = 2
                    select = False
                if button_car3.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    vechicle = 3
                    select = False
                if button_car4.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    vechicle = 4
                    select = False

        x_move = x_mov % background_car.get_rect().width
        SCREEN.blit(background_car,( (x_move - background_car.get_rect().width),72 ))
        if x_move < W:
            SCREEN.blit(background_car,(x_move,72))
        SCREEN.blit(img_cars,(0,0))
        print_buttons(button_back,'BACK',menu_font)
        print_buttons(button_car1,'SELECT',car_font)
        print_buttons(button_car2,'SELECT',car_font)
        print_buttons(button_car3,'SELECT',car_font)
        print_buttons(button_car4,'SELECT',car_font)
        SCREEN.blit(img_cursor,(mouse_pos[0],mouse_pos[1]))
        SCREEN.blit(arcade_menu,(0,0))
        SCREEN.blit(scale(load(join(f_coin,f'Coin_{coin}.png')).convert_alpha(),(220,150)),(370,855))

        x_mov -= 5
        fps_control += 1

        if fps_control % 6 == 0:
            coin += 1
        if coin > 6:
            coin = 1
            fps_control = 0  
        display.update()
    return vechicle                       

def high_score(): # Funcion para mostrar el puntaje mas alto logrado
    hs = True
    coin = 1                                 
    x_mov = 0
    fps_control1 = 0 
    fps_control2 = 0
    bongo = 1
    button_back = Rect(400,690,192,42)
    cat = Rect(710,160,100,100) 
    while hs:
        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  
                if button_back.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    hs = False
                if cat.collidepoint(mouse.get_pos()):
                    sfx_perseo.play()

        print_buttons(cat,':3',menu_font)
        x_move = x_mov % background_h_s.get_rect().width
        SCREEN.blit(background_h_s,( (x_move - background_h_s.get_rect().width),70 ))
        if x_move < W:
            SCREEN.blit(background_h_s,(x_move,70))

        SCREEN.blit(img_hs,(0,0))
        print_buttons(button_back,'BACK',menu_font)
        SCREEN.blit(scale(load(join(f_vfx,f'Bongo_Cat_{bongo}.png')).convert_alpha(),(198,198)),(650,110))
        SCREEN.blit(img_cursor,(mouse_pos[0],mouse_pos[1]))
        SCREEN.blit(arcade_menu,(0,0))
        SCREEN.blit(scale(load(join(f_coin,f'Coin_{coin}.png')).convert_alpha(),(220,150)),(370,855))

        x_mov -= 5
        fps_control1 += 0.5
        fps_control2 += 2

        if fps_control2 % 10 == 0:
            bongo += 1
        if bongo == 21:
            bongo = 1

        if fps_control1 % 6 == 0:
            coin += 1
        if coin > 6:
            coin = 1
            fps_control1 = 0  
        display.update()

def how_to_play(): # Funcion para mostrar la guia de como jugar y los controles
    htp = True
    coin = 1                               
    x_mov = 0
    fps_control = 0
    button_back = Rect(630,670,192,42)
    bonus_1 = Rect(210,580,50,70) 
    bonus_2 = Rect(330,580,50,70) 
    bonus_3 = Rect(460,580,50,70) 
    fuel = Rect(330,440,50,50)  
    while htp:
        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  
                if button_back.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    htp = False
                if bonus_1.collidepoint(mouse.get_pos()):
                    sfx_blood_porky.play()
                if bonus_2.collidepoint(mouse.get_pos()):
                    sfx_blood_oldwoman.play()
                if bonus_3.collidepoint(mouse.get_pos()):
                    sfx_blood_tombos.play()
                if fuel.collidepoint(mouse.get_pos()):
                    sfx_powerup.play()

        print_buttons(bonus_1,'1',menu_font)
        print_buttons(bonus_2,'2',menu_font)
        print_buttons(bonus_3,'3',menu_font)
        print_buttons(fuel,'F',menu_font)
        x_move = x_mov % background_ht_play.get_rect().width
        SCREEN.blit(background_ht_play,( (x_move - background_ht_play.get_rect().width),70 ))
        if x_move < W:
            SCREEN.blit(background_ht_play,(x_move,70))
        SCREEN.blit(img_htp,(0,0))
        print_buttons(button_back,'BACK',menu_font)
        SCREEN.blit(img_cursor,(mouse_pos[0],mouse_pos[1]))
        SCREEN.blit(arcade_menu,(0,0))
        SCREEN.blit(scale(load(join(f_coin,f'Coin_{coin}.png')).convert_alpha(),(220,150)),(370,855))

        x_mov -= 5
        fps_control += 0.5

        if fps_control % 6 == 0:
            coin += 1
        if coin > 6:
            coin = 1
            fps_control = 0  
        display.update()

def credits(): # Funcion para mostrar los creditos del juego
    music.load(join(f_music,'Credits_Music.ogg'))
    music.set_volume(0.5)
    music.play(loops=-1)
    credit = True
    coin = 1
    image = 1                                  
    y_mov = 0
    fps_control = 0
    fps_contro2 = 0 
    button_back = Rect(400,690,192,42)
    cat = Rect(850,500,100,100)  
    while credit:
        CLOCK.tick(60)
        mouse_pos = mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  
                if button_back.collidepoint(mouse.get_pos()):
                    sfx_button_click.play()
                    credit = False
                if cat.collidepoint(mouse.get_pos()):
                    sfx_perseo.play()
                    
        print_buttons(cat,':3',menu_font)
        SCREEN.blit(scale(load(join(f_backgrounds,f'Credits_{image}.png')).convert_alpha(),(1040,701)),(0,80))
        y_move = y_mov % img_credits.get_rect().height
        SCREEN.blit(img_credits,(0, (y_move - img_credits.get_rect().height) ))
        if y_move < H:
            SCREEN.blit(img_credits,(0,y_move))
        SCREEN.blit(scale(load(join(f_backgrounds,f'CreditsT_{image}.png')).convert_alpha(),(1040,701)),(0,80))
        print_buttons(button_back,'BACK',menu_font)
        SCREEN.blit(img_cursor,(mouse_pos[0],mouse_pos[1]))
        SCREEN.blit(arcade_menu,(0,0))
        SCREEN.blit(scale(load(join(f_coin,f'Coin_{coin}.png')).convert_alpha(),(220,150)),(370,855))

        y_mov -= 0.75
        fps_control += 0.5
        fps_contro2 += 1

        if fps_contro2 % 8 == 0:
            image += 1
        if image == 9:
            image = 1

        if fps_control % 6 == 0:
            coin += 1
        if coin > 6:
            coin = 1
            fps_control = 0  
        display.update()
    music.stop()

main_menu() # Iniciamos la funcion menu principal