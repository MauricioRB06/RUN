# Proyecto RUN
# Pygame [ https://www.pygame.org/docs/ ]

# Inicio Pygame y FPS
import pygame, sys
pygame.init()
FPS = 60
RELOJ = pygame.time.Clock()
# Creacion de Pantalla
W,H = 1024,768
SCREEN = pygame.display.set_mode((W,H))

# Fondo del juego
fondo = pygame.image.load('Pixel_Art/Background.png').convert()
y = 0

# Icono y Titulo
pygame.display.set_caption('RUN - The Game')
icono = pygame.image.load('Pixel_Art/Gas.png').convert()
pygame.display.set_icon(icono)

# Persones

# Blucle de juego:
game_over = False
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
	y_movimiento = y % fondo.get_rect().height
	SCREEN.blit(fondo,(0, (y_movimiento - fondo.get_rect().height) ))
	if y_movimiento < H:
		SCREEN.blit(fondo,(0,y_movimiento))

	y -= 3
	RELOJ.tick(FPS)
	pygame.display.update()