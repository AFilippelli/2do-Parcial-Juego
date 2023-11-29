import pygame
from plataforma import Platform  # Asegúrate de importar todas las clases y recursos necesarios
from enemigo import Enemy
from monedas import Coin
from corazon import Corazon
from llave import Key
from player import Player
from constantes import *


class NivelDos:
    def __init__(self, puntaje_nivel1):

        self.level_completed = False

        self.screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.init()


        self.player_1 = Player(x=X,y=Y_LVL2,speed_walk=VELOCIDAD_CAMINAR,speed_run=VELOCIDAD_CORRER ,gravity=GRAVEDAD_PLAYER,jump=SALTO, frame_rate_ms=FRAME_RATE_PLAYER, move_rate_ms=MOVE_RATE_PLAYER,jump_height=ALTURA_SALTO)
        self.player_1.score = puntaje_nivel1


        pygame.font.init()
        self.font = pygame.font.Font(None, TAMAÑO_FUENTE)

        #ENEMIGOS
        self.enemy_list = []
        self.enemy_list.append (Enemy (x=660,y=185,speed_walk=SPEED_WALK2,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS,lifes = VIDAS,can_attack=True))
        self.enemy_list.append (Enemy (x=450,y=445,speed_walk=SPEED_WALK1,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS,lifes = VIDAS,can_attack=True))
        self.enemy_list.append (Enemy (x=850,y=445,speed_walk=SPEED_WALK1,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS,lifes = VIDAS,can_attack=True))
        self.enemy_list.append(Enemy (x=650,y=665,speed_walk=SPEED_WALK2,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS, lifes = VIDAS,can_attack=True))

        #PLATAFORMAS
        self.plataform_list = []
        self.plataform_list.append(Platform(0,230,250,75,platform_type=2)) 
        self.plataform_list.append(Platform(250,230,250,75,platform_type=2)) # x, y, largo, ancho
        self.plataform_list.append(Platform(500,230,300,75,platform_type=3)) 
        self.plataform_list.append(Platform(930,280,70,70,platform_type=0))
        self.plataform_list.append(Platform(1050,370,50,50,platform_type=0))
        self.plataform_list.append(Platform(1135,230,70,75,platform_type=0))
        self.plataform_list.append(Platform(1100,490,200,75,platform_type=3))
        self.plataform_list.append(Platform(900,490,200,75,platform_type=2))
        self.plataform_list.append(Platform(700,490,200,75,platform_type=2))
        self.plataform_list.append(Platform(500,490,200,75,platform_type=2))
        self.plataform_list.append(Platform(300,490,200,75,platform_type=1))
        self.plataform_list.append(Platform(165,600,50,50,platform_type=0))
        self.plataform_list.append(Platform(25,500,50,50,platform_type=0))
        self.plataform_list.append(Platform(280,710,200,75,platform_type=1))
        self.plataform_list.append(Platform(480,710,200,75,platform_type=2))
        self.plataform_list.append(Platform(680,710,200,75,platform_type=2))
        self.plataform_list.append(Platform(880,710,200,75,platform_type=2))
        self.plataform_list.append(Platform(1080,710,220,75,platform_type=2))

        #MONEDAS
        self.coin_list = []
        self.coin_list.append(Coin(x=1155,y=180))
        self.coin_list.append(Coin(x=35,y=450))

        #CORAZONES
        self.heart_list = []
        self.heart_list.append(Corazon(x=945,y=220))
        self.heart_list.append(Corazon(x=1150,y=420))
        self.heart_list.append(Corazon(x=620,y=420))
        self.heart_list.append(Corazon(x=165,y=540))
        self.heart_list.append(Corazon(x=350,y=650))

        #PUNTOS PARA QUE APAREZCA LA LLAVE
        self.points_for_key = PUNTOS_LLAVE_LVL2
        self.key = None
        self.key_collected = False

        #IMAGEN Y POSICION DE LA PUERTA
        self.door_image = pygame.image.load("imagenes/puerta/door1.png")
        self.door_image = pygame.transform.scale(self.door_image, (TAMAÑO_PUERTA))  # tamaño puerta
        self.x_door, self.y_door = UBICACION_PUERTA_LVL2  # posicion puerta

        #IMAGEN DE FONDO
        self.imagen_fondo = pygame.image.load("imagenes/fondo/Battleground1.png")
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))

        #IMAGENES DECORATIVAS
        self.imagenes_fondo = [
        pygame.image.load("imagenes/decoracion/Decor_Statue.png"),
        pygame.image.load("imagenes/decoracion/Decor_Ruins_02.png"),
        pygame.image.load("imagenes/decoracion/Decor_Ruins_01.png"),
        pygame.image.load("imagenes/decoracion/Sign_04.png"),
        pygame.image.load("imagenes/decoracion/Little_Wreckage.png"),
        pygame.image.load("imagenes/decoracion/Sign_05.png")
    ]

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
        if player.score >= self.points_for_key and self.key is None:
            self.key = Key(x=X_LLAVE_LVL2, y=Y_LLAVE_LVL2, points_required=self.points_for_key) 

        if self.key and not player.llave_agarrada:
            if self.key.check_collision(player):
                self.key_pickup_sound.play()
                player.llave_agarrada = True
                self.key_collected = True
                self.level_completed = True  # Marca el nivel como completado

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
        
        pygame.display.flip()