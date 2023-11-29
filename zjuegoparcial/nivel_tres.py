import pygame
from plataforma import Platform  # Asegúrate de importar todas las clases y recursos necesarios
from monedas import Coin
from llave import Key
from corazon import Corazon
from jefe import Boss
from player import Player
from constantes import *


class NivelTres:
    def __init__(self, puntaje_nivel2):

        self.boss_defeated = False
        self.level_completed = False

        self.screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.init()

        self.player_1 = Player(x=X,y=Y_LVL3,speed_walk=VELOCIDAD_CAMINAR,speed_run=VELOCIDAD_CORRER ,gravity=GRAVEDAD_PLAYER,jump=SALTO, frame_rate_ms=FRAME_RATE_PLAYER, move_rate_ms=MOVE_RATE_PLAYER,jump_height=ALTURA_SALTO)
        self.player_1.score = puntaje_nivel2

        pygame.font.init()
        self.font = pygame.font.Font(None, TAMAÑO_FUENTE)

        #ENEMIGOS
        self.enemy_list = []
        self.enemy_list.append(Boss(x=X_BOSS,y=Y_BOSS,speed_walk=SPEED_WALKBOSS,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS,lifes = VIDAS,can_attack=False))

        #PLATAFORMAS
        self.plataform_list = []
        self.plataform_list.append(Platform(1100,600,50,50,platform_type=0))
        self.plataform_list.append(Platform(1000,520,50,50,platform_type=0))
        self.plataform_list.append(Platform(850,520,50,50,platform_type=0))
        self.plataform_list.append(Platform(700,520,50,50,platform_type=0))
        self.plataform_list.append(Platform(550,520,50,50,platform_type=0))
        self.plataform_list.append(Platform(400,520,50,50,platform_type=0))
        self.plataform_list.append(Platform(250,520,50,50,platform_type=0))
        self.plataform_list.append(Platform(150,600,50,50,platform_type=0))
        self.plataform_list.append(Platform(0,700,250,100,platform_type=0))
        self.plataform_list.append(Platform(250,700,250,100,platform_type=0))
        self.plataform_list.append(Platform(500,700,250,100,platform_type=0))
        self.plataform_list.append(Platform(750,700,250,100,platform_type=0))
        self.plataform_list.append(Platform(1000,700,250,100,platform_type=0))
        self.plataform_list.append(Platform(1250,700,250,100,platform_type=0))

        #MONEDAS
        self.coin_list = []
        self.coin_list.append(Coin(x=410,y=450))
        self.coin_list.append(Coin(x=860,y=450))

        #CORAZONES
        self.heart_list = []
        self.heart_list.append(Corazon(x=255,y=450))
        self.heart_list.append(Corazon(x=560,y=450))
        self.heart_list.append(Corazon(x=705,y=450))
        self.heart_list.append(Corazon(x=1000,y=450))

        #PUNTOS PARA QUE APAREZCA LA LLAVE

        self.key = None
        self.key_collected = False

        self.door_image = pygame.image.load("imagenes/puerta/door1.png")
        self.door_image = pygame.transform.scale(self.door_image, (100, 120)) 
        self.x_door, self.y_door = UBICACION_PUERTA_LVL3

        #IMAGEN DE FONDO
        self.imagen_fondo = pygame.image.load("imagenes/fondo/Battleground3.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        #SONIDO AGARRAR ITEMS
        self.coin_pickup_sound = pygame.mixer.Sound("sonidos/agarrar_monedas/agarrar monedas.mp3")
        self.key_pickup_sound = pygame.mixer.Sound("sonidos/agarrar_items/agarrar items.mp3")
        self.key_pickup_sound.set_volume(0.2)

        #sonido curarse
        self.curacion_sound = pygame.mixer.Sound("sonidos/curarse/curarse.mp3")

    def update_enemies(self, delta_ms, player):
        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms, self.plataform_list, self.enemy_list, player)
            if enemy_element.lifes <= 0 and not enemy_element.is_dead:
                enemy_element.take_damage(0, player) #si esta muerto no recibe daño
            for proyectil in enemy_element.proyectiles:
                proyectil.update()

    def draw_enemies(self, screen):
        for enemy_element in self.enemy_list:
            enemy_element.draw(screen)
            for proyectil in enemy_element.proyectiles:
                proyectil.draw(screen)
            # Dibujo de enemigos

    def update_collision_rects(self):
        for enemy_element in self.enemy_list:
            enemy_element.update_collision_rect()


    def update_coins(self,player):
        for coin in self.coin_list:
            if coin.check_collision(player):  # Verificar colisión con el jugador
                player.score += coin.value  # Aumentar la puntuacion al agarrar moneda
                self.coin_pickup_sound.play() #sonido al agarrar moneda
                self.coin_list.remove(coin)  # Eliminar la moneda una vez recolectada

    def draw_coins(self, screen):
        for coin in self.coin_list:
            coin.draw(screen) # Dibujo de monedas


    def update_heart(self,player):
        for heart in self.heart_list:
            if heart.check_collision(player):
                if player.lives < MAX_LIVES:
                    player.lives += heart.heal_amount
                    self.curacion_sound.play()
                    player.score -= SCORE_RESTADO_CORAZON
                    self.heart_list.remove(heart)

    def draw_hearts(self, screen):
        for heart in self.heart_list:
            heart.draw(screen) 


    def update_key(self, player, keys):
        for enemy_element in self.enemy_list:
            if enemy_element.is_dead and self.key is None:
                self.key = Key(x=X_LLAVE_LVL3, y=Y_LLAVE_LVL3 , points_required=0) 
        if self.key and not player.llave_agarrada:
            if self.key.check_collision(player):
                self.key_pickup_sound.play()
                player.llave_agarrada = True
                self.key_collected = True
                self.level_completed = True  # Marca el nivel como completado
                print("nivel completado")

    def draw_key(self, screen):
        screen.blit(self.door_image, (self.x_door, self.y_door)) 
        if self.key and not self.key_collected:
            self.key.draw(screen)
            # Dibujo de la llave


    def update_platform(self,player,platform):
        player.update(self.delta_ms,platform)


    def run_level(self, screen, keys, delta_ms,player_1):

        screen.blit(self.imagen_fondo, self.imagen_fondo.get_rect())

        for plataforma in self.plataform_list:
            plataforma.draw(screen)

        # Actualización y dibujo de enemigos
        self.update_enemies(delta_ms, player_1)
        self.draw_enemies(screen)

        # Actualización y dibujo de monedas
        self.update_coins(player_1)
        self.draw_coins(screen)

        # Actualización y dibujo de la llave
        self.update_key(player_1, keys)
        self.draw_key(screen)

        # Actualización y dibujo de corazones
        self.update_heart(player_1)
        self.draw_hearts(screen)

        # Dibujar puntuación
        score_text = self.font.render(f"Puntuacion: {player_1.score}", True, "white")
        screen.blit(score_text, (UBICACION_PUNTUACION))

        # Resto del código de actualización y dibujo del jugador
        player_1.attack_damage(self.enemy_list)
        player_1.events(keys)
        player_1.update(delta_ms, self.plataform_list, self.enemy_list)
        player_1.draw(screen, self.enemy_list)
        player_1.draw_lives(screen)
        
        