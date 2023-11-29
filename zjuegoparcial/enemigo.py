from player import *
from superficie_sprites import *
from balas import Proyectil
import math

class Enemy():
    def __init__(self, x, y, speed_walk, gravity, frame_rate_ms, move_rate_ms, lifes, can_attack):
        self.walk_l = getSurfaceFromSpriteSheet("imagenes/enemigos/6 Deceased/Deceased_walk.png",6,1)
        self.walk_r = getSurfaceFromSpriteSheet("imagenes/enemigos/6 Deceased/Deceased_walk.png",6,1,True)
        self.hurt = getSurfaceFromSpriteSheet("imagenes/enemigos/6 Deceased/Deceased_hurt.png",2,1)
        self.death = getSurfaceFromSpriteSheet("imagenes/enemigos/6 Deceased/Deceased_death.png",6,1)
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.gravity = gravity
        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tiempo_ultimo_pos = 0
        self.contador = 0
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h -GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)
        self.tiempo_transcurrido_move = 0
        self.lifes = lifes
        self.death_timer = 0
        self.is_dead = False
        self.is_hurt_animation = False
        self.contador_hurt = 0
        self.cooldown = 0
        self.cooldown_max = 2000  # 1000 milisegundos = 1 segundo
        self.proyectiles = []
        self.can_attack = can_attack
        self.attack_sound = pygame.mixer.Sound("sonidos/ataque_enemigos/laser gun.mp3")
        self.attack_sound.set_volume(0.1)  # Ajustar el volumen según sea necesario




    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y

    def do_movement(self, delta_ms, plataform_list):
        if self.lifes > 0 and not self.is_hurt_animation:
            self.tiempo_transcurrido_move += delta_ms
            if self.tiempo_transcurrido_move >= self.move_rate_ms:
                self.tiempo_transcurrido_move = 0
                self.change_x(self.move_x)
                if self.contador <= 35:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1
                elif self.contador <= 70:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0
            
    def do_animation(self, delta_ms):
        if not self.is_dead:
            self.tiempo_transcurrido_animation += delta_ms
            if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
                self.tiempo_transcurrido_animation = 0
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    self.frame = 0



    def update(self, delta_ms, plataform_list, enemy_list, player):
        
        if self.lifes > 0 and not self.is_hurt_animation:
            self.tiempo_transcurrido_move += delta_ms
            if self.tiempo_transcurrido_move >= self.move_rate_ms:
                self.tiempo_transcurrido_move = 0
                self.change_x(self.move_x)
                if self.contador <= 35:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1
                elif self.contador <= 70:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0

        if not self.is_dead:  
            self.check_player_collision(player)
            self.do_movement(delta_ms, plataform_list)
            self.do_animation(delta_ms)
            if not player.is_dead:
                if self.can_attack:
                    dist_horizontal = abs(player.rect.x - self.rect.x)
                    dist_vertical = abs(player.rect.y - self.rect.y + 60)
                    if dist_horizontal < RANGO_DETECCION_HORIZONTAL and dist_vertical < RANGO_DETECCION_VERTICAL and self.cooldown <= 0:
                        self.attack_sound.play()
                        direccion = "izquierda" if player.rect.x < self.rect.x else "derecha"
                        proyectil = Proyectil(self.rect.x, self.rect.y, VELOCIDAD_PROYECTIL, direccion)
                        self.proyectiles.append(proyectil)
                        self.cooldown = self.cooldown_max
                    if self.cooldown > 0:
                        self.cooldown -= delta_ms

                for proyectil in self.proyectiles:
                    proyectil.update()
                    if proyectil.rect.colliderect(player.rect_player):
                        player.take_damage()  # Llama al método del jugador para recibir daño
                        self.proyectiles.remove(proyectil)  # Elimina el proyectil cuando colisiona con el jugador



    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, "red", self.rect)
            pygame.draw.rect(screen, "green", self.rect_ground_collition)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)


    def take_damage(self, damage, player):
        self.lifes -= damage
        

    def update_collision_rect(self):
        pass

    def check_player_collision(self, player):
        if self.rect.colliderect(player.rect_player):
            player.take_damage()  # Llama al método del jugador para recibir daño

