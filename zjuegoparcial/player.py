import pygame
from superficie_sprites import *
from constantes import * 
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

class Player:
    def __init__(self, x, y, speed_walk, speed_run, gravity, jump, frame_rate_ms,move_rate_ms, jump_height) -> None:
        self.walk_r = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Walk.png",9,1)
        self.walk_l = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Walk.png",9,1, True)
        self.stay_r = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Idle.png",5,1)
        self.stay_l = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Idle.png",5,1, True)
        self.jump_r = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Jump.png",7,1)
        self.jump_l = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Jump.png",7,1, True)
        self.run_r = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Run.png", 8,1)
        self.run_l = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Run.png", 8,1, True)
        self.attack_r = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Attack_1.png",4,1)
        self.attack_l = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Attack_1.png",4,1,True)
        self.hurt_r = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Hurt.png",2,1)
        self.hurt_l = getSurfaceFromSpriteSheet("imagenes/jugador/Samurai_Commander/Hurt.png",2,1,True)
        self.corazon_image = pygame.image.load("imagenes/objetos/vida/Life.png")
        self.corazon_image = pygame.transform.scale(self.corazon_image, (40, 40))  # Ajusta el tamaño del corazón según sea necesario
        self.lives = MAX_LIVES
        self.frame = 0
        self.score = START_SCORE
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jumping = jump
        self.animation = self.stay_r
        self.direction = DIRECCION_R
        self.image = self.animation[self.frame] #el personaje hara la animacion
                                                #del frame en particular que elija
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animacion = 0
        self.tiempo_transcurrido_movimiento = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.rect_player = pygame.Rect(self.rect.x + 40, self.rect.y + 60, self.rect.w - 95, self.rect.h - 60)
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 4, self.rect.y + self.rect.h -GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)
        self.rect_attack_on = pygame.Rect(self.rect.x +70, self.rect.y + 50, self.rect.w -60, self.rect.h-100 )
        self.attack_frame = 0
        self.is_attacking_animation = False
        self.attack_cooldown = False
        self.attack_cooldown_time = DELAY_ATAQUE_JUGADOR
        self.attack_coldown_timer = 0
        self.llave_agarrada = False
        self.jump_sound = pygame.mixer.Sound("sonidos/saltar/jump effect.mp3")

        self.attack_sound = pygame.mixer.Sound("sonidos/ataque_espada/Thrall Claw Attack Sound Effect Third Variation.mp3")
        self.attack_sound.set_volume(0.1)  # Esto ajusta el volumen al 50%

        self.walk_sound = pygame.mixer.Sound("sonidos/caminar/Minecraft Footsteps - Sound Effect (HD).mp3")
        self.walk_sound.set_volume(0.2)  # Ajusta el volumen según sea necesario

        self.take_damage_sound = pygame.mixer.Sound("sonidos/take_damage/take damage.mp3")
        self.take_damage_sound.set_volume(0.5)  # Ajusta el volumen según sea necesario

        self.do_damage_sound = pygame.mixer.Sound("sonidos/atacar_enemigo/atacar enemigo.mp3")

        self.damage_cooldown = 1500  # Tiempo de enfriamiento del daño por contacto en milisegundos
        self.last_damage_time = pygame.time.get_ticks()

        self.is_dead = False
        self.tombstone_image = pygame.image.load("imagenes/tumba/tmba.png")
        self.tombstone_image = pygame.transform.scale(self.tombstone_image, (100, 70))


    def walk(self,direction):
        if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
            self.walk_sound.play(-1) #-1 significa que se reproducirá en bucle
            self.frame = 0
            self.direction = direction
            if direction == DIRECCION_R:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l

    def run(self,direction):
        if self.direction != direction or (self.animation != self.run_r and self.animation != self.run_l):
            self.walk_sound.play(-1)
            self.frame = 0
            self.direction = direction
            if direction == DIRECCION_R:
                self.move_x = self.speed_run
                self.animation = self.run_r
            else:
                self.move_x = -self.speed_run
                self.animation = self.run_l

    def attack(self):
        if not self.is_attacking_animation:
            self.attack_sound.play()
            self.is_attacking_animation = True
            self.attack_frame = 0
            if self.direction == DIRECCION_R:
                self.animation = self.attack_r
                self.move_x = 0
            else:
                self.animation = self.attack_l
                self.move_x = 0

    def attack_damage(self, enemy_list):
        if self.is_attacking_animation and not self.attack_cooldown:
            self.attack_cooldown = True
            self.attack_cooldown_timer = pygame.time.get_ticks()
            self.is_attacking_animation = False
            for enemy in enemy_list:
                if self.rect_attack_on.colliderect(enemy.rect):
                    if enemy.lifes > 0 and not enemy.is_dead:  # Verificar si el enemigo está vivo
                        self.do_damage_sound.play()
                        enemy.take_damage(DAÑO, self)
                        enemy.animation = enemy.hurt
                        enemy.frame = 0
                        break  # Romper el bucle después de causar daño

                    if enemy.lifes <= 0 and not enemy.is_dead:
                        # Si el enemigo se queda sin vidas, cambiar la animación a "death"
                        self.score += SCORE_ENEMIGOS
                        enemy.is_dead = True
                        enemy.animation = enemy.death
                        enemy.frame = 0

                        print("Enemigo herido")


    def jump(self, on_off=True):
        if on_off and self.is_jump == False:
            self.jump_sound.play()  # Reproducir el sonido de salto con un retraso de 100 milisegundos
            self.y_start_jump = self.rect.y
            if self.direction == DIRECCION_R:
                self.move_y = -self.jumping
                self.move_x = self.speed_walk
                self.animation = self.jump_r
            else:
                self.move_y = -self.jumping
                self.move_x = -self.speed_walk
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if on_off == False:
            self.is_jump = False
            self.stay()

    def stay(self):
        if self.animation != self.stay_r and self.animation != self.stay_l:
            self.walk_sound.stop()
            if self.direction == DIRECCION_R:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def movimiento(self,delta_ms,lista_plataformas): #establecer un movimiento
        self.tiempo_transcurrido_movimiento += delta_ms
        if self.tiempo_transcurrido_movimiento >= self.move_rate_ms:
            if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0
            self.tiempo_transcurrido_movimiento = 0
            self.add_x(self.move_x)
            self.add_y(self.move_y)

            if self.is_on_platform(lista_plataformas) == False:
                self.add_y(self.gravity)
            elif self.is_jump:
                self.jump(False)

    def is_on_platform(self,lista_plataformas):
        retorno = False
        if self.rect.y >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if self.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
                    retorno = True
                    break
        return retorno

    def add_x(self, delta_x):
        self.rect.x += delta_x
        self.rect_player.x += delta_x
        self.rect_ground_collition.x += delta_x #hitbox de pies
        self.update_attack_hitbox(delta_x)

        #CODIGO PARA NO SALIRSE DEL MAPA
        if self.rect.right > ANCHO_VENTANA + 50: #ajustes necesarios para mi tipo de pantalla
            self.rect.right = ANCHO_VENTANA + 50
            self.rect_player.right = ANCHO_VENTANA 
            self.rect_ground_collition.right = ANCHO_VENTANA 
            self.rect_attack_on.right = ANCHO_VENTANA + 50
        elif self.rect.left < -50:
            self.rect.left = -50
            self.rect_player.left = 0
            self.rect_ground_collition.left = 0
            self.rect_attack_on.left = -50

    def add_y(self, delta_y):
        self.rect.y += delta_y
        self.rect_player.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.update_attack_hitbox(delta_y)

    def animacion(self, delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms
        if self.tiempo_transcurrido_animacion >= self.frame_rate_ms:
            self.tiempo_transcurrido_animacion = 0
            if self.is_attacking_animation:
                if self.attack_frame < len(self.animation) - 1:
                    self.attack_frame += 1
                else:
                    self.is_attacking_animation = False
                    self.attack_frame = 0
                    self.animation = self.walk_r if self.move_x != 0 else self.stay_r if self.direction == DIRECCION_R else self.walk_l if self.move_x != 0 else self.stay_l
            else:
                if (self.frame < len(self.animation) - 1):
                    self.frame += 1
                else:
                    self.frame = 0

    def update(self, delta_ms, lista_plataformas, enemies):
        if not self.is_dead:
            self.movimiento(delta_ms, lista_plataformas)
            self.animacion(delta_ms)

            # Actualizar el temporizador de bloqueo temporal
            if self.attack_cooldown:
                current_time = pygame.time.get_ticks()
                if current_time - self.attack_cooldown_timer > self.attack_cooldown_time:
                    self.attack_cooldown = False

            if self.rect.y >= ALTURA_MUERTE:
                self.lives = 0
                self.is_dead = True


    def update_attack_hitbox(self, delta):
        self.rect_attack_on.y = self.rect.y + 65
        self.rect_attack_on.width = self.rect.w - 70
        self.rect_attack_on.height = self.rect.h - 110
        # Ajusta la posición de la hitbox de ataque según la dirección
        if self.direction == DIRECCION_R:
            self.rect_attack_on.x = self.rect.x + 70
        else:
            self.rect_attack_on.x = self.rect.x 

    def draw(self, screen, enemies):
        if DEBUG:
            pygame.draw.rect(screen, "red", self.rect_player)
            pygame.draw.rect(screen, "green", self.rect_ground_collition)
            pygame.draw.rect(screen,"blue", self.rect_attack_on)

        if self.is_dead:
            screen.blit(self.tombstone_image, self.rect)
        else:
            if self.is_attacking_animation:
                if self.attack_frame < len(self.animation):
                    self.image = self.animation[self.attack_frame]
                    screen.blit(self.image, self.rect)
                    for enemy in enemies:
                        if self.rect_player.colliderect(enemy.rect):
                            enemy

            else:
                if self.frame < len(self.animation):
                    self.image = self.animation[self.frame]
                    screen.blit(self.image, self.rect)

    def draw_lives(self, screen):
        x = 10
        y = 10
        for vida in range(self.lives):
            screen.blit(self.corazon_image, (x, y))
            x += 50  # Espacio entre los corazones

    def take_damage(self):
        current_time = pygame.time.get_ticks()  # Tiempo actual en milisegundos
        if current_time - self.last_damage_time > self.damage_cooldown:
            self.lives -= 1  # Reduce las vidas del jugador
            self.take_damage_sound.play()
            self.last_damage_time = current_time  # Actualiza el último tiempo de daño aplicado
            print("Player takes damage!")  # Mensaje para verificar el daño
            if self.lives <= 0:
                    self.is_dead = True  # Cambiar el estado a "muerto" si las vidas son iguales o menores a cero
                    self.rect.y = self.rect.y + 60 # Establecer la posición de la tumba en el suelo
                    self.rect.x = self.rect.x  # Ajustar la posición de la tumba para que se vea correctamente

    def events(self, keys ):
        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and keys[pygame.K_RIGHT]:
            self.walk(DIRECCION_R)
            self.jump()
        elif (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and keys[pygame.K_LEFT]:
            self.walk(DIRECCION_L)
            self.jump()
        elif keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            self.stay()
        elif keys[pygame.K_z]:
            self.attack()  
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT]:
            self.run(DIRECCION_R)
        elif keys[pygame.K_LSHIFT] and  keys[pygame.K_LEFT]:
            self.run(DIRECCION_L)
        elif (keys[pygame.K_UP] or keys[pygame.K_SPACE]) :
            self.jump()
        elif keys[pygame.K_UP] or keys[pygame.K_SPACE] and keys[pygame.K_z]:
            self.jump()
            self.attack()
        elif keys[pygame.K_RIGHT]:
            self.walk(DIRECCION_R)
        elif keys[pygame.K_LEFT] :
            self.walk(DIRECCION_L)
            
        else:
            self.stay()
