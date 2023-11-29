import pygame
from plataforma import Platform  # Asegúrate de importar todas las clases y recursos necesarios
from enemigo import Enemy
from monedas import Coin
from llave import Key
from corazon import Corazon
from jefe import Boss
from player import Player
from nivel_dos import NivelDos
from constantes import *

class NivelUno:
    def __init__(self):

        self.level_completed = False

        self.screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.init()


        self.player_1 = Player(x=X,y=Y_LVL1,speed_walk=VELOCIDAD_CAMINAR,speed_run=VELOCIDAD_CORRER ,gravity=GRAVEDAD_PLAYER,jump=SALTO, frame_rate_ms=FRAME_RATE_PLAYER, move_rate_ms=MOVE_RATE_PLAYER,jump_height=ALTURA_SALTO)



        pygame.font.init()
        self.font = pygame.font.Font(None, TAMAÑO_FUENTE)

        #ENEMIGOS
        self.enemy_list = []
        self.enemy_list.append(Enemy (x=750,y=655,speed_walk=SPEED_WALK ,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS, lifes = VIDAS,can_attack=False))
        self.enemy_list.append (Enemy (x=350,y=435,speed_walk=SPEED_WALK ,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS,lifes = VIDAS,can_attack=False))
        self.enemy_list.append (Enemy (x=650,y=435,speed_walk=SPEED_WALK ,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS,lifes = VIDAS,can_attack=False))
        self.enemy_list.append (Enemy (x=630,y=245,speed_walk=SPEED_WALK ,gravity=GRAVITY,frame_rate_ms=FRAME_RATE_MS,move_rate_ms=MOVE_RATE_MS,lifes = VIDAS,can_attack=False))
        #self.enemy_list.append(Boss(x=750,y=450,speed_walk=4,gravity=8,frame_rate_ms=10,move_rate_ms=20,lifes = 3,can_attack=True))


        #PLATAFORMAS
        self.plataform_list = []
        self.plataform_list.append(Platform(-10,700,176,75,platform_type=2)) 
        self.plataform_list.append(Platform(166,700,166,75,platform_type=2)) # x, y, largo, ancho
        self.plataform_list.append(Platform(332,700,166,75,platform_type=3)) 
        self.plataform_list.append(Platform(600,700,125,75,platform_type=1))
        self.plataform_list.append(Platform(725,700,125,75,platform_type=3))
        self.plataform_list.append(Platform(950,675,100,50,platform_type=0))
        self.plataform_list.append(Platform(1150,600,75,50,platform_type=0))
        self.plataform_list.append(Platform(975,515,75,50,platform_type=0))
        self.plataform_list.append(Platform(1150,440,75,50,platform_type=0))
        self.plataform_list.append(Platform(200,480,225,50,platform_type=1))
        self.plataform_list.append(Platform(425,480,225,50,platform_type=2))
        self.plataform_list.append(Platform(650,480,225,50,platform_type=3))
        self.plataform_list.append(Platform(50,390,75,50,platform_type=0))
        self.plataform_list.append(Platform(200,290,215,50,platform_type=1))
        self.plataform_list.append(Platform(415,290,215,50,platform_type=2))
        self.plataform_list.append(Platform(630,290,215,50,platform_type=3))
        self.plataform_list.append(Platform(950,230,150,50,platform_type=1))
        self.plataform_list.append(Platform(1100,230,150,50,platform_type=3))



        #MONEDAS
        self.coin_list = []
        self.coin_list.append(Coin(x=75,y=350))
        self.coin_list.append(Coin(x=1170,y=400))

        #CORAZONES
        self.heart_list = []
        self.heart_list.append(Corazon(x=1165,y=540))
        self.heart_list.append(Corazon(x=750,y=420))
        self.heart_list.append(Corazon(x=420,y=420))
        self.heart_list.append(Corazon(x=300,y=230))

        #PUNTOS PARA QUE APAREZCA LA LLAVE
        self.points_for_key = PUNTOS_LLAVE_LVL1
        self.key = None
        self.key_collected = False

        #IMAGEN Y POSICION DE LA PUERTA
        self.door_image = pygame.image.load("imagenes/puerta/door1.png")
        self.door_image = pygame.transform.scale(self.door_image, (TAMAÑO_PUERTA))  # tamaño puerta
        self.x_door, self.y_door = UBICACION_PUERTA_LVL1  # posicion puerta
    
        #IMAGEN DE FONDO
        self.imagen_fondo = pygame.image.load("imagenes/fondo/Battleground4.png")
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
        self.imagen_decoracion = self.imagenes_fondo[0]
        self.imagen_decoracion = pygame.transform.scale(self.imagen_decoracion,(300,250)) #ancho, alto
        self.imagen_cartel_calavera = self.imagenes_fondo[3]
        self.imagen_cartel_calavera = pygame.transform.scale(self.imagen_cartel_calavera,(75,75))
        self.imagen_cartel_exclamacion = self.imagenes_fondo[5]
        self.imagen_cartel_exclamacion = pygame.transform.scale(self.imagen_cartel_exclamacion,(75,75))
        self.imagen_piedra = self.imagenes_fondo[4]
        self.imagen_piedra = pygame.transform.scale(self.imagen_piedra,(110,130))


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
                enemy_element.take_damage(0, player)
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
            self.key = Key(x=X_LLAVE_LVL1, y=Y_LLAVE_LVL1, points_required=self.points_for_key)
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

    def run_level(self, screen, keys, delta_ms, player_1):
        screen.blit(self.imagen_fondo, self.imagen_fondo.get_rect())


        # Dibujar elementos del nivel
        screen.blit(self.imagen_decoracion, (500, 45))
        screen.blit(self.imagen_cartel_calavera, (962, 602))
        screen.blit(self.imagen_cartel_exclamacion, (760, 627))
        screen.blit(self.imagen_piedra, (270, 351))
        
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
        score_text = self.font.render(f"Puntuacion: {player_1.score}", True, "black")
        screen.blit(score_text, (UBICACION_PUNTUACION))

        # Resto del código de actualización y dibujo del jugador
        player_1.attack_damage(self.enemy_list)
        player_1.events(keys)
        player_1.update(delta_ms, self.plataform_list, self.enemy_list)
        player_1.draw(screen, self.enemy_list)
        player_1.draw_lives(screen)
        
        pygame.display.flip()