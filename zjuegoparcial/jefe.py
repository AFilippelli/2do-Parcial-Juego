import pygame
from enemigo import Enemy
from superficie_sprites import *

class Boss(Enemy):
    def __init__(self, x, y, speed_walk, gravity, frame_rate_ms, move_rate_ms, lifes, can_attack):
        super().__init__(x, y, speed_walk, gravity, frame_rate_ms, move_rate_ms, lifes, can_attack)
        self.walk_l = getSurfaceFromSpriteSheet("imagenes/jefe/Walk (3).png",6,1)
        self.walk_r = getSurfaceFromSpriteSheet("imagenes/jefe/Walk (3).png",6,1,flip=True)
        self.death = getSurfaceFromSpriteSheet("imagenes/jefe/Death.png",6,1)
        
        self.lifes = lifes * 3 # multiplicador de vida del enemigo para el jefe
        self.rect_boss = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y , self.rect.w +100, self.rect.h +150)
        
        self.x = x
        self.y = y

    def update(self, delta_ms, plataform_list, enemy_list, player):
        super().update(delta_ms, plataform_list, enemy_list, player)

        if self.lifes > 0 and not self.is_hurt_animation:
            # Calcula la dirección hacia la que debe moverse el jefe
            if player.rect.x < self.rect.x:
                self.move_x = -self.speed_walk  # Si el jugador está a la izquierda, el jefe se mueve a la izquierda
                self.animation = self.walk_l
            elif player.rect.x > self.rect.x:
                self.move_x = self.speed_walk  # Si el jugador está a la derecha, el jefe se mueve a la derecha
                self.animation = self.walk_r
            else:
                self.move_x = 0  # Si el jugador está en la misma posición X, el jefe no se mueve
            # Aplica el movimiento
            self.change_x(self.move_x)
        if self.lifes <= 0:
            self.is_dead = True
            self.animation = self.death
            self.image = self.animation[self.frame]


    def update_collision_rect(self):
        self.rect_boss =  pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y , self.rect.w +100, self.rect.h +150)
