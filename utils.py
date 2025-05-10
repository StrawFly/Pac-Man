import pygame
from config import TAM_CELDA

def hay_colision(rect, mapa):
    puntos = [
        (rect.left, rect.top),
        (rect.right - 1, rect.top),
        (rect.left, rect.bottom - 1),
        (rect.right - 1, rect.bottom - 1)
    ]
    for x, y in puntos:
        fila = y // TAM_CELDA
        col = x // TAM_CELDA
        if fila < 0 or fila >= len(mapa) or col < 0 or col >= len(mapa[0]):
            return True
        if mapa[fila][col] == 1:
            return True
    return False


def mostrar_texto(pantalla, texto, tam, color, pos):
    import pygame
    fuente = pygame.font.SysFont("arial", tam, bold=True)
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect(center=pos)
    pantalla.blit(superficie, rect)


def mostrar_puntos(pantalla, puntos, color, ancho):
    import pygame
    fuente = pygame.font.SysFont("arial", 24, bold=True)
    texto = fuente.render(f"Puntos: {puntos}", True, color)
    rect = texto.get_rect(center=(ancho // 2, 20))
    pantalla.blit(texto, rect)

