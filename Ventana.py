# Proyecto R.U.N
# Pygame [ https://www.pygame.org/docs/ ]

# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 													  #
#	   Proyecto Final Pogramacion de Computadores     #
#													  #
#	   Universidad Nacional de Colombia - 2020 II     #
#	       Docente: Juan Diego Escobar Mejia          #
#	                 Programadores: 			      #
# 													  #
#	 Mauricio Rodriguez Becerra  - Ing. Mecatronica   #
#	 Laura Alejandra Paez Daza   - Ing. Mecatronica   #
#	 Alejandro Mendivelso Torres - Ing. Mecatronica   #
#	 Juan Esteban Flechas Rincon - Ing. Electronica   #
#												      #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pygame, sys
import random
from random import choice 

# Clases Jugador / Enemigo / Items
class Player(pygame.sprite.Sprite): # Heredamos de pygame - modulo sprite - clase Sprite

	def __init__(self,vehicle_select): # Creamos el constructor

		# Creacion de Sprites para el Personaje
		vehicle_1 = pygame.image.load('Pixel_Art/Vechicles/Vehicle_01.png').convert_alpha()
		vehicle_2 = pygame.image.load('Pixel_Art/Vechicles/Vehicle_02.png').convert_alpha()
		vehicle_3 = pygame.image.load('Pixel_Art/Vechicles/Vehicle_03.png').convert_alpha()
		vehicle_4 = pygame.image.load('Pixel_Art/Vechicles/Vehicle_04.png').convert_alpha()

		# Heredamos del constructor de Sprite
		super().__init__()

		# Crear rectangulo del jugador
		if vehicle_select == 1:
			self.image = vehicle_1
		elif vehicle_select == 2:
			self.image = vehicle_2
		elif vehicle_select == 3:
			self.image = vehicle_3
		elif vehicle_select == 4:
			self.image = vehicle_4

		self.rect = self.image.get_rect() # Obtener la medida del rectangulo en base a la imagen
		self.rect.center = ( 1024 // 2, 690 ) # Posición inicial del jugador

	def update(self): # Actualización de la clase en cada vuelta del bucle

		self.velocidad = 0 # Velocidad predeterminada en caso de no presionar ninguna tecla
		tecla = pygame.key.get_pressed() # Para revisar si una tecla esta pulsada

		if tecla[pygame.K_LEFT]:  # Si se pulsa la tecla izquierda
			self.velocidad = -6
		if tecla[pygame.K_RIGHT]: # Si se pulsa la tecla derecha
			self.velocidad = +6	
		
		self.rect.x += self.velocidad # Actualiza la velocidad del personaje
		
		if self.rect.left < 230: # Limitar Movimiento por la Izquierda
			self.rect.left = 230
		if self.rect.right > 996: # Limitar Movimiento por la derecha
			self.rect.right = 996
class Enemy(pygame.sprite.Sprite):

	def __init__(self): # Creamos el constructor

		# Creacion de Sprites Enemigos 
		enemy_1 = pygame.image.load('Pixel_Art/Enemies/Enemy_01.png').convert_alpha()
		enemy_2 = pygame.image.load('Pixel_Art/Enemies/Enemy_02.png').convert_alpha()
		enemy_3 = pygame.image.load('Pixel_Art/Enemies/Enemy_03.png').convert_alpha()
		enemy_4 = pygame.image.load('Pixel_Art/Enemies/Enemy_04.png').convert_alpha()
		enemy_5 = pygame.image.load('Pixel_Art/Enemies/Enemy_05.png').convert_alpha()
		enemy_6 = pygame.image.load('Pixel_Art/Enemies/Enemy_06.png').convert_alpha()
		enemigos = [ enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6 ]

		# Posiciones de los carriles
		carril_1 = ( 260,0 )
		carril_2 = ( 350,0 )
		carril_3 = ( 465,0 )
		carril_4 = ( 555,0 )
		carril_5 = ( 667,0 )
		carril_6 = ( 757,0 )
		carril_7 = ( 870,0 )
		carril_8 = ( 960,0 )
		carriles = [ carril_1, carril_2, carril_3, carril_4, carril_5, carril_6, carril_7, carril_8]

		# Heredamos del constructor de Sprite
		super().__init__()

		# Crear rectangulo del enemigo
		self.image = choice(enemigos)
		self.rect = self.image.get_rect() # Obtener la medida del rectangulo en base a la imagen
		self.rect.center = choice(carriles)
		self.velocidad = 5

	def update(self):

		self.rect.y += self.velocidad # Actualizar la velocidad del enemigo
	
class Gas(pygame.sprite.Sprite):

	def __init__(self): # Creamos el constructor

		# Creacion de Sprites Item
		item_1 = pygame.image.load('Pixel_Art/Items/Gas.png').convert_alpha()
		pos_gas = int(random.randint(250, 950))

		# Heredamos del constructor de Sprite
		super().__init__()

		# Crear rectangulo para la gasolina
		self.image = item_1
		self.rect = self.image.get_rect() # Obtener la medida del rectangulo en base a la imagen
		self.rect.center = (pos_gas,-50)

# Inicio Pygame
pygame.init()

# Creacion de Pantalla
RELOJ = pygame.time.Clock()
FPS = 60
W,H = 1024,768
SCREEN = pygame.display.set_mode((W,H))

# Icono y Titulo
pygame.display.set_caption('RUN - The Game')
icono = pygame.image.load('Pixel_Art/icon.png').convert_alpha()
pygame.display.set_icon(icono)

# Fondo del juego
background = pygame.image.load('Pixel_Art/Backgrounds/Background.png').convert_alpha()
y = 0

# Creacion de grupos de Sprites, instanciación de objetos
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

enemigo_1 = Enemy()
enemigos.add(enemigo_1)

Jugador = Player(1)
sprites.add(Jugador)

enemigo_2 = Enemy()
enemigos.add(enemigo_2)

gasolina = Gas()
sprites.add(gasolina)

enemigo_3 = Enemy()
enemigos.add(enemigo_3)

# Blucle de juego:
game = True
while game:

	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()

	y_move = y % background.get_rect().height
	SCREEN.blit(background,(0, (y_move - background.get_rect().height) ))
	if y_move < H:
		SCREEN.blit(background,(0,y_move))

	sprites.update() # Actualización de sprites
	enemigos.update()

	colision = pygame.sprite.spritecollide(Jugador,enemigos,False)
	if colision:
		enemigo_1.kill()
	elif enemigo_1.rect.top > H:
		enemigo_1.kill()
	elif enemigo_1.rect.top > H:
		enemigo_2.kill()
	elif enemigo_1.rect.top > H:
		enemigo_3.kill()

	sprites.draw(SCREEN) # Dibujo de los sprites en pantalla
	enemigos.draw(SCREEN)

	y += 5
	RELOJ.tick(FPS)
	pygame.display.update()