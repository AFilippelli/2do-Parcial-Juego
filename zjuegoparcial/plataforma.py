import pygame
from superficie_sprites import *
from constantes import *

class Platform:
    def __init__(self,x,y,width,height,platform_type):
        self.platform_images = [
            getSurfaceFromSpriteSheet("imagenes/plataformas/Ground_02.png", 1, 1),
            getSurfaceFromSpriteSheet("imagenes/plataformas/Ground_10.png", 1, 1),
            getSurfaceFromSpriteSheet("imagenes/plataformas/Ground_11.png", 1, 1),
            getSurfaceFromSpriteSheet("imagenes/plataformas/Ground_12.png", 1, 1)
        ]

        self.image = self.platform_images[platform_type]


        if isinstance(self.image, list) and len(self.image) > 0:  # verificar que sea una lista y que no esté vacia
            self.image = pygame.transform.scale(self.image[0], (width, height)) 
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, GROUND_RECT_H)
        else:
            print("Failed to load platform image!")  # Notify if there's an issue loading the image

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,"red",self.rect)
        screen.blit(self.image, self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,"green",self.rect_ground_collition)

            