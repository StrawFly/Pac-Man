import pygame
from config import TAM_CELDA, AMARILLO
from utils import hay_colision

class Pacman:
    def __init__(self, x, y):
        self.radio = TAM_CELDA // 2 - 6
        self.rect = pygame.Rect(0, 0, self.radio*2, self.radio*2)
        self.rect.center = (x*TAM_CELDA + TAM_CELDA//2, y*TAM_CELDA + TAM_CELDA//2)
        self.direccion = pygame.Vector2(0, 0)
        self.velocidad = 2

    def mover(self):
        nuevo_rect = self.rect.move(self.direccion.x, self.direccion.y)
        if not hay_colision(nuevo_rect):
            self.rect = nuevo_rect

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, AMARILLO, self.rect.center, self.radio)
