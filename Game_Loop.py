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
# SYS [ https://docs.python.org/3/library/sys.html ]

import pygame
from pygame.sprite import Group
from pygame.mixer import music
from os.path import join
from sys import exit
from Directorys_Settings import SCREEN,FPS,CLOCK,H,f_music,sfx_low_fuel,game_map1_1,game_map1_2,img_low_fuel,arcade_game
from Game_functions import score_print, pause, crash, busted, game_over  # Importamos las funciones que usaremos del módulo[ Game_functions ]
from Game_class import Player, Enemy, Police_siren, Fuel, Score_goal     # Importamos las clases que usaremos del módulo [ Game_class ]

# ----------------------------------------- Inicializar Pygame y Pygame Mixer -------------------------

pygame.init()         # Inicializamos pygame
pygame.mixer.init()   

# ----------------------------------------- Funcion del juego ----------------------------------------- 

def game_loop(car): # Blucle del juego

	carriles = [ 156, 233, 313, 390, 470, 546, 627, 703, 783, 861 ] # Creamos las posiciones que usaremos en X para definir los carriles

	
	players = Group() # el metodo Group() nos permite crear un grupo que contendra todos los sprites que pertenezcan a dicho grupo
	enemies = Group() # para esto es importante que la clase tenga el constructor ( Super.__init__() ) del metodo sprite que es quien nos permite usar este metodo con nuestros objetos
	fuel = Group()    # Creacion de grupos de Sprites para poder revisar colisiones y dibujar y actualizar todos los sprites dentro del grupo al mismo tiempo
	score_goal = Group()
	police_siren = Group()

	player = Player(car) # Creamos una instanciación de la clase jugador, la cual recibe como parametro el auto seleccionado por el jugador
	players.add(player)  # agregamos al grupo de sprites jugadores, el objeto jugador que acabamos de crear

	goal = Score_goal()  # Creamos una instanciación de la clase Meta que usaremos para calcular el puntaje
	score_goal.add(goal) 

	siren = Police_siren() # Creamos una instanciación de la clase sirena, que usaremos para mostrar una animacion en la parte inferior de la pantalla como si nos estuvieran persiguiendo
	police_siren.add(siren)

	game = True
	music.load(join(f_music,'Game_Music.ogg'))
	music.set_volume(0.7) 
	music.play(loops=-1)
	sfx_low_fuel.set_volume(0.05) # El metodo set_volume() nos ayuda a reducir o aumentar el volumen de los sonidos, entre 0 y 1
	score = 0                     # Iniciamos el puntaje en 0
	remaining_fuel= 219           # Creamos la cantidad inicial de combustible que tendra el jugador
	mov_y = 0                     # Variable para mover el fondo ( la imagen del mapa en este caso )

	while game:

		CLOCK.tick(FPS) 

		if not fuel:       # Si no existen objetos en el grupo gasolina, se crean
			gas = Fuel()   # en este caso creamos un solo objeto
			fuel.add(gas)  # lo agregamos al grupo de sprites
		
		if not enemies:                   # Si no existen objetos en el grupo enemigos, se crean
			for i in carriles:            # en este caso creamos enemigos, igual a la cantidad de carriles que tengamos creados
				enemy_type = Enemy(i)     # y se envia a cada enemigo una posicion de carril distinta para que se cree un enemigo por cada carril
				enemies.add(enemy_type)   # lo vamos agregando al grupo de sprites enemigos, conforme se van creando

		for event in pygame.event.get():
			if event.type == pygame.QUIT: exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.mixer.music.set_volume(0.2)
					pause()   # Cuando presionamos la tecla Space, llamamos a la funcion que pausa el juego
					pygame.mixer.music.set_volume(0.7)			
 
		y_move = mov_y % game_map1_1.get_rect().height                           # Creamos una variable que obtiene el resto de la pantalla por mover ( respecto al ancho en este caso )
		SCREEN.blit(game_map1_1,(0, (y_move - game_map1_1.get_rect().height) ))  # pintamos la imagen con las nuevas coordenada ( la que cambia es la Y entonces movemos de arriba a abajo )
		if y_move < H:                                                           # si la imagen llega hasta el final de la pantalla
			SCREEN.blit(game_map1_1,(0,y_move))                                  # se imprime de nuevo, en la posicion original creando asi el bucle infinito de movimiento

		recharge = pygame.sprite.spritecollide(player,fuel,False)  # creamos la variable recharge que sera True si se cumplen las condiciones
		if recharge:
			sfx_low_fuel.stop()
			if car == 1:                    # ya que la dificultad se ajusta en la clase dependiendo del carro que seleccione el jugador
				score += 50                 # recargar gasolina se vuelve mas complicado, entre mas lento sea el carro, la recarga da mas puntaje
			elif car == 2:                  
				score += 100
			elif car == 3:
				score += 200
			else:
				score += 300
			gas.recharge()                  # llamamos al metodo recharge de la clase Fuel() el cual nos reposiciona la gasolina
			if remaining_fuel <= 50:
				remaining_fuel += 50
			elif remaining_fuel <= 150:
				remaining_fuel += 25
			else: 
				remaining_fuel += 219-remaining_fuel

		colision = pygame.sprite.spritecollide(player,enemies,False) # creamos la variable colision que sera True si se cumplen las condiciones
		if colision:   # Si se produce la colision entre el sprite del jugador y un sprite del grupo enemigos, llamamos a la animacion busted y a la funcion game_over
			sfx_low_fuel.stop() 
			crash(game_map1_1,(0, (y_move - game_map1_1.get_rect().height)-15 ),game_map1_2,(0, (y_move - game_map1_2.get_rect().height)-15 ),players,enemies,police_siren,player.rect.x,player.rect.y)
			game_over(0,score)
			game = False # despues de salir de la animacion y "menu" de game_over se pone game en false para salir del bucle while del juego
			
		if remaining_fuel <= 0:  # Si la gasolina es  igual o menor 0, llamamos a la animacion busted y a la funcion game_over
			music.stop()
			busted(game_map1_1,(0, (y_move - game_map1_1.get_rect().height)-15 ),game_map1_2,(0, (y_move - game_map1_2.get_rect().height)-15 ),players,enemies,police_siren)
			game_over(1,score)
			game = False

		players.update()  # Llamamos al metodo update() que definimos en cada clase, para que actualize los esprites depentiendo de la configuracion que hicimos en el update() de cada una
		fuel.update()
		enemies.update()
		score_goal.update()
		police_siren.update()

		win_score = pygame.sprite.spritecollide(goal,enemies,False,False) # si los enemigos colisionan con el sprite de la meta de puntuacion, generan puntos cada vez que colisionen
		if win_score:                                                     # entonces entre mas grande el enemigo ( tamaño del rectangulo ), colisiona por mas tiempo y genera mas puntos
			if car == 1:                                                  # ya que la dificultad se ajusta en la clase dependiendo del carro que seleccione el jugador
				score += 1                                                # los autos 1 y 2 son los mas rapidos para moverse entonces generan menos puntos ya que es mas facil esquivar
			elif car == 2:                                                # y los autos 3 y 4 se mueven mas lento, por lo tanto generan mas puntos ya que es mas dificil esquivar
				score += 1
			elif car == 3:
				score += 2
			else:
				score += 2
		
		players.draw(SCREEN)  # Ya que actualizamos los prites y comprobamos las colisiones ahora dibujaremos los sprites en pantalla
		enemies.draw(SCREEN)
		fuel.draw(SCREEN)
		police_siren.draw(SCREEN)
		score_goal.draw(SCREEN)

		y_move = mov_y % game_map1_2.get_rect().height
		SCREEN.blit(game_map1_2,(0, (y_move - game_map1_2.get_rect().height) ))
		if y_move < H:
			SCREEN.blit(game_map1_2,(0,y_move))
		SCREEN.blit(arcade_game,(0,0))
		
		if remaining_fuel > 1 and remaining_fuel <=70:                             # Si la gasolina es menor a 70
			music.set_volume(0.4)                                                  # Bajamos el volumen de la musica
			sfx_low_fuel.play()                                                    # reproducimos el sonido de alerta de poca gasolina
			SCREEN.blit(img_low_fuel,(185,150))                                    # mostramos en pantalla la imagen de alerta poca gasolina
			pygame.draw.rect(SCREEN,(200,100,100),(418, 941, remaining_fuel, 15))  # imprimimos en pantalla un rectangulo, en la superficie SCREEN, del color indicado, en la posicion y tamaño indicado
		elif remaining_fuel > 70 and remaining_fuel <=149:                         # Si la gasolina esta entre 70 y 149
			music.set_volume(0.7)                                                  # Dejamos el volumen normal
			pygame.draw.rect(SCREEN,(252,209,42),(418, 941, remaining_fuel, 15))   
		else:                                                                      # Si la gasolina es mayor a 150
			music.set_volume(0.7)
			pygame.draw.rect(SCREEN,(100,200,100),(418, 941, remaining_fuel, 15))  

		remaining_fuel -= 0.06  # reducimos la gasolina al final de cada ejecución
		score_print(SCREEN,str(score).zfill(10),540,900,(0,0,0),20)  # Una vez impresas todas las imagenes, imprimimos el puntaje para que quede encima de todas las capas y sea visible
		mov_y += 15
		pygame.display.update()
	return score # al terminar el juego y que game = False , entonces como final de la funcion game_loop() retornamos el puntaje que nos dio el juego para usarlo