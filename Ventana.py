# Proyecto RUN
# Pygame [ https://www.pygame.org/docs/ref/key.html ]

import pygame, sys
import random
from random import choice 

#comentario de prueba

#Constantes
ANCHO = 1024
ALTO = 768
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)

#Carriles 
carril_1=250
carril_2=400
carril_3=650
carril_4=900
carriles=[carril_1,carril_2,carril_3,carril_4]

#jugador
jugador_size = 50
jugador_pos = [ANCHO / 2, ALTO - jugador_size * 2]

#Enemigo(s)
enemigo_size = 100
enemigo_pos = [choice(carriles),0]

#random.randint(0,ANCHO - enemigo_size)

#ventana
ventana = pygame.display.set_mode((ANCHO,ALTO))
game_over = False
clock = pygame.time.Clock()

#Funciones
def detectar_colision(jugador_pos,enemigo_pos):
	jx = jugador_pos[0]
	jy = jugador_pos[1]
	ex = enemigo_pos[0]
	ey = enemigo_pos[1]

	if (ex >= jx and ex <(jx + jugador_size)) or (jx >= ex and jx < (ex + enemigo_size)):
		if (ey >= jy and ey <(jy + jugador_size)) or (jy >= ey and jy < (ey + enemigo_size)):
			return True
		return False


while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			x = jugador_pos[0]
			if event.key == pygame.K_LEFT:
				x -= jugador_size
			if event.key == pygame.K_RIGHT:
				x += jugador_size

			jugador_pos[0] = x
	ventana.fill(color_negro)

	if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
		enemigo_pos[1] += 20
	else:
		enemigo_pos[0] = int(choice(carriles))
		enemigo_pos[1] = 0

	#Colisiones
	if detectar_colision(jugador_pos,enemigo_pos):
		game_over = True

	#Dibujar enemigo
	pygame.draw.rect(ventana, color_azul ,(enemigo_pos[0],enemigo_pos[1],enemigo_size, enemigo_size))
	

	#Dibujar jugador
	pygame.draw.rect(ventana, color_rojo,
			(jugador_pos[0],jugador_pos[1],
			jugador_size,jugador_size))
	clock.tick(30)
	pygame.display.update()