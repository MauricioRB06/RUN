import pygame, sys

# Iniciacion de Pygame y FPS
pygame.init()
FPS = 60
RELOJ = pygame.time.Clock()

# Creación Pantalla - Ventana
W,H = 1024,768
SCREEN = pygame.display.set_mode((W,H))

# Fondo del juego
fondo = pygame.image.load('Pixel_Art/Background.png').convert() # .convert() para optimizar la imagen y no relentize el juego
y = 0 # Moveremos el fondo en el eje Y para dar la sensacion de movimiento

# Icono y Titulo de ventana
pygame.display.set_caption('RUN - The Game')
icono = pygame.image.load('Pixel_Art/gas.png')
pygame.display.set_icon(icono)

# Personaje

# Bucle de ejecucion del juego
game_over = False
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	y_movimiento = y % fondo.get_rect().height
	SCREEN.blit(fondo, (0, y_movimiento - fondo.get_rect().height) )
	if y_movimiento < H:
		SCREEN.blit(fondo,(0,y_movimiento))

	y -= 5
	pygame.display.update()
	RELOJ.tick(FPS)
