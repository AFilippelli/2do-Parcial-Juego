from superficie_sprites import *
import pygame

class Proyectil:
    def __init__(self, x, y, velocidad, direccion):
        self.image = pygame.image.load("imagenes/objetos/balas/5.png")
        self.image = pygame.transform.scale(self.image, (15, 15)) #ancho, alto
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad
        self.direccion = direccion

    def update(self):
        if self.direccion == "izquierda":
            self.rect.x -= self.velocidad
        elif self.direccion == "derecha":
            self.rect.x += self.velocidad
        # Resto de la lógica para otras direcciones

    def draw(self, screen):
        screen.blit(self.image, self.rect)