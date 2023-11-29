from superficie_sprites import *
from constantes import *
class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load("imagenes/objetos/moneda/Coin_01.png")# Ajusta la ruta de la imagen de la moneda
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.value = 1000 # Valor de la moneda, puedes ajustarlo según desees

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, "red", self.rect)

    def check_collision(self, player):
        if self.rect.colliderect(player.rect_player):
            return True
        else: 
            return False