import pygame
from superficie_sprites import *

class Key:
    def __init__(self, x, y, points_required):
        self.key_image = pygame.image.load("imagenes/objetos/llave/Key_01.png")
        self.key_image = pygame.transform.scale(self.key_image, (60, 30)) #ancho, alto
        self.key_appear_sound = pygame.mixer.Sound("sonidos/obtener_llave/zelda item.mp3")
        self.key_appear_sound.set_volume(0.5)  # Ajustar volumen 
        self.sound_played = False

        self.key_rect = self.key_image.get_rect()
        self.key_rect.x = x
        self.key_rect.y = y

        self.door_rect = pygame.Rect(1100, 135, 70, 110)  # Ajusta el tamaño y la posición según tu diseño
        self.points_required = points_required  # Puntos necesarios para obtener la llave
        self.collected = False
        
    def draw(self, screen):
        screen.blit(self.key_image, self.key_rect)
        if not self.collected and not self.sound_played:
            self.key_appear_sound.play()
            self.sound_played = True

    def check_collision(self, player):
        if self.key_rect.colliderect(player.rect):
            if not self.collected:
                self.collected = True
                return True
        return False