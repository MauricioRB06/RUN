import pygame
from pygame.locals import *
import sys

class Entrada():


    def __init__(self):
        self.lineas = 0
        self.caracteres = [' ', ]
        self.fuente = pygame.font.Font(None, 25)


        self.distancia = 20
        self.pos_x = 50
        self.pos_y = 50


    def teclas(self, evento):
        for accion in evento:
            if accion.type == KEYDOWN:
                if accion.key == K_RETURN:
                    print(accion.type)
                    self.caracteres.append('')
                    self.lineas += 1
                elif accion.key == K_ESCAPE:
                    sys.exit(0)
                elif accion.key == K_BACKSPACE:
                    if self.caracteres[self.lineas] == '' and self.lineas > 0:
                        self.caracteres = self.caracteres[0:-1]
                        self.lineas -= 1
                    else:
                        self.caracteres[self.lineas] = self.caracteres[self.lineas][0:-1]
                else:
                    self.caracteres[self.lineas] = str(
                        self.caracteres[self.lineas] + accion.unicode)


    def mensaje(self, superficie):
        superficie.fill((0, 0, 0))
        for self.lineas in range(len(self.caracteres)):
            img_letra = self.fuente.render(
                self.caracteres[self.lineas], True, (200, 200, 200))
            superficie.blit(
                img_letra, (self.pos_x, self.pos_y + self.distancia * self.lineas))

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Escribir en pygame')
    salir = False


    entrar_texto = Entrada()


    while not salir:
        eventos = pygame.event.get()
        for accion in eventos:
            if accion.type == pygame.QUIT:
                salir = True


        entrar_texto.teclas(eventos)
        entrar_texto.mensaje(pantalla)
        pygame.display.update()

main()