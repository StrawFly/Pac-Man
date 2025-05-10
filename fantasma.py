import pygame
import random
from config import TAM_CELDA, ROJO
from utils import hay_colision

class Fantasma:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x*TAM_CELDA, y*TAM_CELDA, TAM_CELDA, TAM_CELDA)
        self.velocidad = 2
        self.direccion = pygame.Vector2(self.velocidad, 0)

    def mover(self):
        if self.en_interseccion():
            opciones = [
                pygame.Vector2(self.velocidad, 0),
                pygame.Vector2(-self.velocidad, 0),
                pygame.Vector2(0, self.velocidad),
                pygame.Vector2(0, -self.velocidad)
            ]
            opciones = [op for op in opciones if op != -self.direccion]
            random.shuffle(opciones)
            for dir in opciones:
                nuevo_rect = self.rect.move(dir.x, dir.y)
                if not hay_colision(nuevo_rect):
                    self.direccion = dir
                    break
        nuevo_rect = self.rect.move(self.direccion.x, self.direccion.y)
        if not hay_colision(nuevo_rect):
            self.rect = nuevo_rect

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, ROJO, self.rect)

    def en_interseccion(self):
        return self.rect.x % TAM_CELDA == 0 and self.rect.y % TAM_CELDA == 0
