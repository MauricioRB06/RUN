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
# RANDOM [ https://docs.python.org/3/library/random.html ]

import pygame                      # Importamos el paquete pygame
from pygame.sprite import Sprite
from pygame.image import load
from pygame.mixer import Sound
from os.path import join
from random import choice, randint # Importamos las funciones que usaremos del módulo [ random ]
 # Importamos las variables y directorios que usaremos del módulo [ Directorys_Settings ]
from Directorys_Settings import H, f_vehicles, f_enemies, f_items, f_vfx, f_sfx, sfx_powerup, sfx_blood_tombos
from Directorys_Settings import sfx_blood_porky,sfx_blood_oldwoman, img_bonus_1, img_bonus_2,img_bonus_3

# ----------------------------------------- Clases = Jugador / Enemigo / Items / Animaciones -----------------------------------------

class Player(Sprite): # Clase Jugador - Nuestra clase Hereda de pygame - modulo sprite - clase Sprite

	# El contructor y los Metodos siempre nos piden escribir explitamente el objeto a recibir, en python se especifica con la palabra: self
	def __init__(self,vehicle_select): # Constructor - Solicitamos El Vehiculo Seleccionado
		self.level = vehicle_select    # Asignar dificultad en base al auto escogido
		super().__init__()             # Heredamos el constructor de la clase Sprite
		self.image = load(join(f_vehicles,f'Vehicle_0{vehicle_select}.png')).convert_alpha() # Asignar imagen al sprite del jugador en base al vehiculo seleccionado
		self.rect = self.image.get_rect()     # Creacion del rectangulo para colisiones en base a tamaño de la imagen del sprite
		self.rect.center = ( 1024 // 2, 690 ) # Posición inicial del jugador

	def update(self):  # Metodo - Actualización del objeto en cada vuelta del bucle del juego ( game_loop )

		self.speed = 0 # Velocidad predeterminada en caso de no presionar ninguna tecla
		tecla = pygame.key.get_pressed() # Creamos una variable para revisar si una tecla esta pulsada 

		if tecla[pygame.K_LEFT]:         # Si se pulsa la tecla flecha izquierda
			self.speed= -(8-self.level)  # Cantidad de pixeles que se movera en -X el sprite cuando se presione la tecla ( sera mas o menos, dependiendo la dificultad )
		if tecla[pygame.K_RIGHT]:        # Si se pulsa la tecla flecha derecha
			self.speed = 8-self.level    # Cantidad de pixeles que se movera en +X el sprite cuando se presione la tecla ( sera mas o menos, dependiendo la dificultad )

		self.rect.x += self.speed # Actualiza la posicion en base a la velocidad del personaje

		if self.rect.left < 119:  # Limitar Movimiento por la Izquierda para que no se salga del dibujo de la via
			self.rect.left = 119  # Si se llega al tope siempre se dibujara en la misma posicion
		if self.rect.right > 895: # Limitar Movimiento por la derecha para que no se salga del dibujo de la via
			self.rect.right = 895 # # Si se llega al tope siempre se dibujara en la misma posicion

class Enemy(Sprite): # Clase Enemigo
	
	enemies_image = []  # Creamos una lista que contenga a todos los sprites posibles de los enemigos ( Propiedades de la clase )
	for num in range(0,16):
		enemy = load(join(f_enemies,f'Enemy_{num}.png')).convert_alpha() # usamos la variable for para ir cambiando el nombre del archivo que se agregara
		enemies_image.append(enemy) # Al ser una lista usamos el metodo append() para agregar cada sprite nuevo a la lista

	def __init__(self,num_carril): 
		super().__init__()
		self.image = choice(self.enemies_image) # Asignamos una imagen aleatoria de la lista cada que se crea un enemigo
		self.rect = self.image.get_rect()
		self.rect.center = ( randint((num_carril-6),(num_carril+6)), -(randint(200,550))) # Posicion Inicial = centramos el rectangulo en X con el carril y en Y aleatoreamente, para que se creen en distintas posiciones
		self.speed = randint(6,10) # asignamos una velocidad de desplazamiento inicial aleatoria, para que todos los enemigos tengan distintas velocidades
		self.new_pos = num_carril  # creamos una variable para obtener la posicion del carril al momento de la creacion del objeto enemigo

	def update(self):

		self.rect.y += self.speed     # Actualizar la velocidad del enemigo en base a la velocidad creada
		if self.rect.top > H:         # Si el enemigo se sale de la pantalla se vuelve a posicionar y actualza sus valores para dar la impresion de que es un "nuevo enemigo"
			self.speed = randint(6,10) # Genera un valor disinto de velocidad, para que siempre que se salga de la pantalla obtenga una velocidad diferente
			self.image = choice(self.enemies_image) # Asignamos una imagen aleatorea para que siempre que se salga de la pantalla obtenga una imagen diferente
			self.rect = self.image.get_rect()       # Actualizamos el rectangulo al nuevo sprite
			self.rect.center = ( randint((self.new_pos-6),(self.new_pos+6)), -(randint(200,550)) ) # Se centra el rectangulo en una nueva posicion cuando se salga de la pantalla

class Fuel(Sprite): # Clase Gasolina

	frames =[]  # Creamos una lista que contenga a todos los sprites posibles para la gasolina ( Propiedades de la clase )
	for num in range(0,6):
		frame = pygame.image.load(join(f_items,f'Fuel_{num}.png')).convert_alpha()
		frames.append(frame)

	def __init__(self):
		super().__init__() 
		self.image = choice(self.frames)
		self.rect = self.image.get_rect()
		self.rect.center = (randint(145,876),-3000) # Centramos el rectangulo dentro de la zona de los carriles en X y a -3000 pixeles del top de la pantalla en Y
		self.speed = 8

	def update(self):
		self.rect.y += self.speed
		self.image = choice(self.frames)
		if self.rect.top > ( H+3000 ): # Si la gasolina se sale de la pantalla + 3000 pixeles
			self.rect.center = (randint(145,876),-3000) # Cuando da la vuelta se reinicia su posicion de forma aleatorea dentro de la zona de los carriles

	def recharge(self):
		sfx_powerup.play() # Usamos el metodo .play() de la clase Sound() para reproducir el archivo de sonido
		self.rect.center = (randint(145,876),-4500) # Como la posicion donde puede chocar con el jugador es mas corta, se regenera mas lejos para que no salga tan rapido

class Score_goal(Sprite): # Clase Meta para Puntuacion

	def __init__(self):
		super().__init__()
		self.image = load(join(f_enemies,'Score_goal.png')).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (500,800)

	def update(self):
		self.rect.center = (500,800)

class Police_siren(Sprite): # Clase para Animacion sirena de policia

	sirens =[]
	for num in range(1,7):
		siren = load(join(f_vfx,f'siren_{num}.png')).convert_alpha()
		sirens.append(siren)

	def __init__(self):
		super().__init__()
		self.image = choice(self.sirens)
		self.rect = self.image.get_rect()
		self.rect.center = (500,500)

	def update(self):
		self.image = choice(self.sirens)
class Bonus(Sprite):  # Clase Objeto bonus

	def __init__(self):
		super().__init__() 
		self.option = randint(1,3)
		if self.option  == 1:
			self.image = img_bonus_1
		elif self.option  == 2:
			self.image = img_bonus_2
		else:
			self.image = img_bonus_3
		self.rect = self.image.get_rect()
		self.rect.center = (randint(145,876),-4000) # Centramos el rectangulo dentro de la zona de los carriles en X y a -3000 pixeles del top de la pantalla en Y
		self.speed = 8

	def update(self):
		self.rect.y += self.speed
		if self.rect.top > ( H+4000 ):
			self.option = randint(1,3)
			if self.option  == 1:
				self.image = img_bonus_1
				self.rect = self.image.get_rect()
			elif self.option  == 2:
				self.image = img_bonus_2
				self.rect = self.image.get_rect()
			else:
				self.image = img_bonus_3
				self.rect = self.image.get_rect()
			self.rect.center = (randint(145,876),-4000)

	def kill_bonus(self):
		if self.option == 1:
			sfx_blood_porky.play()
		elif self.option == 2:
			sfx_blood_oldwoman.play()
		else:
			sfx_blood_tombos.play()
		bonus_kill = self.option
		self.option = randint(1,3)
		if self.option  == 1:
			self.image = img_bonus_1
			self.rect = self.image.get_rect()
		elif self.option  == 2:
			self.image = img_bonus_2
			self.rect = self.image.get_rect()
		else:
			self.image = img_bonus_3
			self.rect = self.image.get_rect()
		self.rect.center = (randint(145,876),-8000)
		return bonus_kill
		
class Blood(Sprite): # Clase para Animacion Sangre

	def __init__(self,x,y):
		super().__init__()
		self.kill_anim = []
		for num in range(1,6):
			blood = load(join(f_vfx,f'Blood_{num}.png')).convert_alpha()
			blood = pygame.transform.scale(blood,(100,100))
			self.kill_anim.append(blood)
		self.index = 0                          # Esta variable nos ayuda a recorrer las posiciones de la lista
		self.image = self.kill_anim[self.index] # Siempre se crea la animacion desde la primera imagen
		self.rect = self.image.get_rect()
		self.rect.center = [x+50,y+100]
		self.counter = 0                         # Este contador nos ayuda la cantidad de veces que se ha reproducido la animacion

	def update(self):

		blood_speed = 6		     # Podemos controlar la velocidad de reproduccion de la animacion
								 # Actualizar la animación
		self.counter += 1        # Agregamos un valor a la cantidad de reproducciones de la imagen
		self.center = (500,500)  # Centramos la animacion, en donde estaba el sprite colisionado  
		if self.counter >= blood_speed and self.index < len(self.kill_anim) - 1:  # Si el contador de reproduccion es mayoy a la velocidad de reproduccion, cambiamos la imagen a la siguiente de la lista
			self.counter =0
			self. index += 1
			self.image = self.kill_anim[self.index]
		
		if self.index >= len(self.kill_anim) -1 and self.counter >= blood_speed: # Si la animación llego al final de las imagenes de la lista entonces la terminamos
			self.kill() # Con el metodo .kill() destuimos y borramos el objeto