# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 													  #
# 				    Proyecto R.U.N					  #
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
# SYS [ https://docs.python.org/3/library/sys.html ]

import pygame
from pygame.image import load
from pygame.mixer import Sound, music
from pygame.font import Font
from pygame import display
from os.path import join
from time import sleep # Importamos las funciones que usaremos del módulo [ time ]
from sys import exit   # Importamos las funciones que usaremos del módulo [ sys ]
from Directorys_Settings import SCREEN,FPS,CLOCK,W,H,f_music,f_gameover,f_vfx,sfx_crash,sfx_busted
from Directorys_Settings import arcade_pause,arcade_game_over,arcade_lose,img_pause,img_busted,img_crash,img_go_0,img_go_1,background_go

# En este caso no deseamos pre-cargar muchas de la imagenes que aqui salen, ya que con cada actualizacion estas cambian, para simular animación, asi que se decicio por cargarlas en tiempo real

# ----------------------------------------- Funciones = Imprimir texto / Pausar / Choque / Arresto / Game_Over -----------------------------------------

def score_print(SCREEN,score,x,y,color,size): # Funcion para imprimir la puntuación en pantalla
	score_font = Font('04B30.ttf', size)          # Creamos un objeto de la clase Font() que usaremos como fuente para imprimirla en pantalla, usamos el archivo .ttf ubicado en la carpeta raiz y un tamaño
	surface = score_font.render(score,True,color) # Creamos una superficie para poner el texto y mostrarlo en pantalla, especificamos el texto, True para usar anti-aliased y el color del texto
	size_text = surface.get_rect()                # Creamos el rectangulo en base al tamaño final de la superficie ( que cambiara cada vez que cambie el texto )
	size_text.center = (x,y)                      # Centramos el rectangulo en la posicion deseada de la pantalla
	SCREEN.blit(surface,size_text)                # en la ventana SCREEN con el metodo .blit() dibujamos una superficie ( el texto ) del tamaño del texto final de esta ( el rectangulo)
	
def hg_score(final_score): # Funcion para guardar el puntaje maximo logrado
	pass

def pause(): # Funcion para pausar el juego
	pause = True
	while pause:
		CLOCK.tick(10)
		for event in pygame.event.get():          # Esta funcion recorre todos los eventos que van sucediendo
			if event.type == pygame.QUIT: exit()  # Si el evento llamado es evento salir ( por ejemplo presionando la X de la ventana ), cierra el programa
			if event.type == pygame.KEYDOWN:      # Si el evento llamado es oprimir una tecla, se procede a revisar
				if event.key == pygame.K_SPACE:   # Si la tecla, es espacio, sale del bucle de pausa, si no, continua el bucle
					pause = False		
		SCREEN.blit(img_pause,(0,0))              # el metodo .blit() cambiara un poco su comportamiento dependiendo de los parametros que ingresemos
		SCREEN.blit(arcade_pause,(0,0))           # en este caso estamos unicamente ingresando la imagen como superficie y la pocicion donde se debe imprimir
		display.update()						  # el metodo update() del modulo display, nos permite actualizar la pantalla, para mostrar los cambios realizados en cada ejecución

def crash(exp_b1,b1_pos,exp_b2,b2_pos,player,enemies,siren,p_x,p_y): # Funcion para animación al chocar

	music.stop()   # El metodo stop() nos permite detener la reprodución de la musica de fondo
	crash = True
	fps_6 = 0      
	sfx_crash.play()  # El metodo play() de la clase Sound() nos permite reproducir un sonido
	while crash:
		CLOCK.tick(8) # Asignamos la frecuencia de actualización de la ventana, en este caso8 porque las animaciones tienen pocos frames, para que no se reproduzcan tan rapido
		for event in pygame.event.get():
			if event.type == pygame.QUIT: exit()
		SCREEN.blit(exp_b1,(b1_pos))	
		player.draw(SCREEN) # El metodo draw() nos permite dibujar en este caso, un sprite o grupo de sprites en una superficie en este caso SCREEN
		enemies.draw(SCREEN)
		SCREEN.blit(load(join(f_vfx,f'explosion_{fps_6}.png')).convert_alpha(),(p_x-30,p_y-9))
		SCREEN.blit(exp_b2,(b2_pos))
		siren.draw(SCREEN)
		SCREEN.blit(img_crash,(0,0))	
		SCREEN.blit(arcade_game_over,(0,0))	
		display.update()
		fps_6 +=1
		if fps_6 == 7:
			crash = False	
	player.draw(SCREEN)
	enemies.draw(SCREEN)
	SCREEN.blit(load(join(f_vfx,'explosion_3.png')).convert_alpha(),(p_x-30,p_y-9)) 
	SCREEN.blit(exp_b2,(b2_pos))
	siren.draw(SCREEN)
	SCREEN.blit(img_crash,(0,0))	
	SCREEN.blit(arcade_lose,(0,0))	
	display.update()
	sleep(1) # La funcion sleep() nos permite pausar la ejecución del programa, durante un tiempo determinado en milisegundos
	
def busted(exp_b1,b1_pos,exp_b2,b2_pos,player,enemies,siren): # Funcion para animación al ser capturado por quedar sin gasolina
	music.stop()
	busted = True
	sfx_busted.play()
	while busted:
		CLOCK.tick(8)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: exit()
		SCREEN.blit(exp_b1,(b1_pos))	
		player.draw(SCREEN)		
		enemies.draw(SCREEN)
		SCREEN.blit(exp_b2,(b2_pos))
		siren.draw(SCREEN)
		SCREEN.blit(img_busted,(0,0))	
		SCREEN.blit(arcade_lose,(0,0))		
		display.update()
		sleep(7)
		busted = False

def game_over(why,score): # Funcion para llamar a la animacion y "menu" game over al terminar la partida
	g_over = True
	why = why
	music.load(join(f_music,'Game_Over_Music.ogg')) # el metodo load() nos permite al igual que con imagenes cargar un archivo de sonido para reproducirlo como musica de fondo
	music.play(loops=-1) # El parametro loops = x nos permite decirle la cantidad de veces que necesitamos que se reproduzca la musica, si dejamos en -1 se reproducira infinitamente
	music.set_volume(0.7)  # El metodo set_volume() nos ayuda a reducir o aumentar el volumen de la musica, entre 0 y 1
	fps_4 = 1
	fps_8 = 1
	mov_x = 0
	while g_over:
		CLOCK.tick(8)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					g_over = False

		x_move = mov_x % background_go.get_rect().width 							  # Creamos una variable que obtiene el resto de la pantalla por mover ( respecto al ancho en este caso )
		SCREEN.blit(background_go,( (x_move - background_go.get_rect().width),70 ))   # pintamos la imagen con las nuevas coordenada ( la que cambia es la X entonces movemos de izquierda a derecha )
		if x_move < W:                                                                # si la imagen llega hasta el final de la pantalla
			SCREEN.blit(background_go,(x_move,70)) 									  # se imprime de nuevo, en la posicion original creando asi el bucle infinito de movimiento
		
		if why == 1:
			SCREEN.blit(img_go_1,(0,0))
			SCREEN.blit(load(join(f_gameover,f'Policecar_01_{fps_8}.png')).convert_alpha(),(50,460))
			SCREEN.blit(load(join(f_gameover,f'Policecar_02_{fps_8}.png')).convert_alpha(),(590,450))
			SCREEN.blit(load(join(f_gameover,f'Policeman_{fps_4}.png')).convert_alpha(),(475,510))
			SCREEN.blit(load(join(f_gameover,f'Men_{fps_4}.png')).convert_alpha(),(450,535))
		else:
			SCREEN.blit(img_go_0,(0,0))
			SCREEN.blit(load(join(f_vfx,f'Fire_01_{fps_8}.png')).convert_alpha(),(580,400))
			SCREEN.blit(load(join(f_vfx,f'Smoke_{fps_8}.png')).convert_alpha(),(510,450))
			SCREEN.blit(load(join(f_vfx,f'Fire_02_{fps_4}.png')).convert_alpha(),(415,570))

		score_print(SCREEN,str(score).zfill(10),720,180,(236,219,83),30)  # el metodo .zfill() nos ayuda a rellenar con 0 un texto
		SCREEN.blit(arcade_game_over,(0,0))
		fps_4 += 1
		fps_8 += 1
		mov_x += 15 # Esta es la cantidad de pixeles que se va a desplazar el fondo en cada ejecución entre mas, se movera mas rapido
		if fps_4 == 5:
			fps_4 = 1
		if fps_8 == 9:
			fps_8 = 1
		display.update()
	SCREEN.fill((0,0,0)) # Al salir del game over, para que no se muestre como quedo la posicion de los enemigos y demas cuando se pauso el juego al perder, pintamos todo de negro y salimos


def puntaje ():

    Best = [5,4,4,9,8,10,5000]

    print(max([int(num) for num in Best]))

puntaje()
