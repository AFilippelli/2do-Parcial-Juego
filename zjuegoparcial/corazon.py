import pygame

class Corazon:
    def __init__(self, x, y):
        self.heart_image = pygame.image.load("imagenes/objetos/vida/Life.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (40, 40))
        self.rect = self.heart_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.heal_amount = 1  # Cantidad de vida que el corazón devuelve al jugador
        
    def draw(self, screen):
        screen.blit(self.heart_image, self.rect)
        # pygame.draw.rect(screen, "red", self.rect)  # Puedes descomentar esta línea para ver el rectángulo del corazón en pantalla

    def check_collision(self, player):
        if self.rect.colliderect(player.rect_player):
            return True
        else: 
            return False