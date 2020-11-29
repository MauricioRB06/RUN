# Proyecto RUN
# Pygame  [ https://www.pygame.org/docs/ ] 

import pygame
import sys
import random
from random import choice 

pygame.font.init()

#Constantes
ANCHO = 1024
ALTO = 768
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)
color_verde = (0,255,0)
color_blanco = (255,255,255)

#Carriles 
carril_1=250
carril_2=400
carril_3=650
carril_4=900
carriles=[carril_1,carril_2,carril_3,carril_4]

#jugador
jugador_size = 50
jugador_pos = [ANCHO / 2, ALTO - jugador_size * 2]
gasolina = 100
puntaje = 0

#Enemigo(s)
enemigo_size = 100
enemigo_pos = [choice(carriles),0]

#random.randint(0,ANCHO - enemigo_size)

#Galon gasolina
galon_size = 40
galon_pos = [random.randint(0,ANCHO - galon_size),0]

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

def puntaje_en_pantalla(lugar, texto, size, x, y):
    font = pygame.font.SysFont("serif", size)
    texto_surface = font.render(texto, True, color_blanco)
    texto_rect = texto_surface.get_rect()
    texto_rect.midtop=(x,y)
    lugar.blit(texto_surface, texto_rect)

def bGasolina(gasolina):
	x=50
	y=9.5
	pygame.draw.rect(ventana, color_blanco,(47,6.5,106,26),3)
	pygame.draw.rect(ventana, color_verde, (x, y, gasolina, 20))	

def recarga_gasolina(jugador_pos):
	global galon_pos
	jx = jugador_pos[0]
	jy = jugador_pos[1]
	gx = galon_pos[0]
	gy = galon_pos[1]

	if (gx >= jx and gx <(jx + jugador_size)) or (jx >= gx and jx < (gx + galon_size)):
		if (gy >= jy and gy <(jy + jugador_size)) or (jy >= gy and jy < (gy + galon_size)): 
			galon_pos[1]=ALTO
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

	if enemigo_pos[1]>ALTO:
		puntaje+=1
		if game_over==True:
			puntaje_final=puntaje

	if gasolina<=0:
		game_over=True
		continue

	if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
		enemigo_pos[1] += 20
	else:
		enemigo_pos[0] = int(choice(carriles))
		enemigo_pos[1] = 0

	#Colisiones
	if detectar_colision(jugador_pos,enemigo_pos):
		game_over = True

	#Desplazamiento galon de gasolina
	if galon_pos[1] >= 0 and galon_pos[1] < 2000:
		galon_pos[1] += 7
	else:
		galon_pos[0] = random.randint(0,ANCHO - galon_size)
		galon_pos[1] = 0

	#Recarga de gasolina

	if recarga_gasolina(jugador_pos):
		if gasolina<=90:
			gasolina+=10
		else: 
			gasolina+=100-gasolina		

	#Dibujar enemigo
	pygame.draw.rect(ventana, color_azul ,(enemigo_pos[0],enemigo_pos[1],enemigo_size, enemigo_size))
	
	#Dibujar jugador
	pygame.draw.rect(ventana, color_rojo,
			(jugador_pos[0],jugador_pos[1],
			jugador_size,jugador_size))

	#Dibujar galon gasolina
	gas = pygame.image.load('Pixel_Art/Items/Gas.png')
	ventana.blit(gas,(galon_pos[0],galon_pos[1]))

	"""pygame.draw.rect(ventana, color_verde,
			(galon_pos[0],galon_pos[1],
			galon_size, galon_size))"""

		#Dibujar enemigo
	pygame.draw.rect(ventana, color_azul,
			(enemigo_pos[0],enemigo_pos[1],
			enemigo_size, enemigo_size))


	icono_gas = pygame.image.load('Pixel_Art/Gas_icono.png')
	ventana.blit(icono_gas,(10,5))	
	bGasolina(gasolina)	
	gasolina-=0.04
	puntaje_en_pantalla (ventana, str(puntaje), 50, ANCHO/2, 10)
	clock.tick(30)
	pygame.display.update()
