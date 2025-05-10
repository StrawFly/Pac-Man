import pygame, sys, random
from config import *
from laberinto import laberinto
from pacman import Pacman
from fantasma import Fantasma
from utils import obtener_posiciones_libres, mostrar_texto, mostrar_puntos
from utils import FILAS, COLUMNAS

FILAS = len(laberinto)
COLUMNAS = len(laberinto[0])
ANCHO, ALTO = COLUMNAS * TAM_CELDA, FILAS * TAM_CELDA

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pac-Man")
reloj = pygame.time.Clock()

def dibujar_mapa():
    for y, fila in enumerate(laberinto):
        for x, celda in enumerate(fila):
            if celda == 1:
                pygame.draw.rect(pantalla, AZUL, (x*TAM_CELDA, y*TAM_CELDA, TAM_CELDA, TAM_CELDA))

# Puntos
puntos = [pygame.Rect(x*TAM_CELDA + TAM_CELDA//3, y*TAM_CELDA + TAM_CELDA//3, 10, 10)
          for y, fila in enumerate(laberinto) for x, celda in enumerate(fila) if celda == 0]

# Pantalla de inicio
jugando = False
puntos_actuales = 0
while not jugando:
    pantalla.fill(NEGRO)
    mostrar_texto(pantalla, "PAC - MAN", 48, AMARILLO, ANCHO, ALTO, -50)
    mostrar_texto(pantalla, "Presiona ESPACIO para iniciar", 28, BLANCO, ANCHO, ALTO, 20)
    pygame.display.update()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            jugando = True

# Crear jugador y fantasmas
pos_libres = obtener_posiciones_libres()
pacman = Pacman(*random.choice(pos_libres))
fantasmas = [Fantasma(*random.choice(pos_libres)) for _ in range(2)]

# Bucle principal
while True:
    pantalla.fill(NEGRO)
    dibujar_mapa()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                pacman.direccion = pygame.Vector2(-pacman.velocidad, 0)
            elif evento.key == pygame.K_RIGHT:
                pacman.direccion = pygame.Vector2(pacman.velocidad, 0)
            elif evento.key == pygame.K_UP:
                pacman.direccion = pygame.Vector2(0, -pacman.velocidad)
            elif evento.key == pygame.K_DOWN:
                pacman.direccion = pygame.Vector2(0, pacman.velocidad)

    pacman.mover()
    for fantasma in fantasmas:
        fantasma.mover()

    nuevos_puntos = []
    for punto in puntos:
        if pacman.rect.colliderect(punto):
            puntos_actuales += 2
        else:
            nuevos_puntos.append(punto)
    puntos = nuevos_puntos

    for punto in puntos:
        pygame.draw.rect(pantalla, BLANCO, punto)

    mostrar_puntos(pantalla, puntos_actuales, ANCHO)
    pacman.dibujar(pantalla)
    for fantasma in fantasmas:
        fantasma.dibujar(pantalla)

    for fantasma in fantasmas:
        if pacman.rect.colliderect(fantasma.rect):
            pantalla.fill(NEGRO)
            mostrar_texto(pantalla, "GAME OVER", 60, ROJO, ANCHO, ALTO)
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

    if not puntos:
        pantalla.fill(NEGRO)
        mostrar_texto(pantalla, "WINN", 60, AMARILLO, ANCHO, ALTO)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    reloj.tick(FPS)
