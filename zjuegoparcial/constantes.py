import pygame
ANCHO_VENTANA = 1300
ALTO_VENTANA = 800

#IZQUIERA = 0, DERECHA = 1
DIRECCION_L = 0
DIRECCION_R = 1

#FUENTE
TAMAÑO_FUENTE = 42

#PUNTUACION
UBICACION_PUNTUACION = 300, 15

#PARA LAS HITBOXS
DEBUG = False

#HITBOX DE LAS PLATAFORMAS
GROUND_RECT_H = 5

#TECHO Y PUSO DEL JUEGO
GROUND_LEVEL = 800

TOP_LEVEL = -50
DAÑO = 1 #recibido y hecho

#RANGO ENEMIGOS DETECCION PARA DISPARAR
RANGO_DETECCION_VERTICAL = 50 
RANGO_DETECCION_HORIZONTAL = 400 

VELOCIDAD_PROYECTIL = 3  #proyectiles enemigos

#CORAZONES
SCORE_RESTADO_CORAZON = 200

#JUGADOR DATOS
MAX_LIVES = 5  #vidas
START_SCORE = 0 #puntaje al iniciar
DELAY_ATAQUE_JUGADOR = 700 #tiempo entre cada golpe del jugador
SCORE_ENEMIGOS = 500 #el puntaje que le daran los enemigos a mi jugador al morir
ALTURA_MUERTE = 700 #si mi personaje supera el valor 700 en y, muere
VELOCIDAD_CAMINAR = 4
VELOCIDAD_CORRER = 8
GRAVEDAD_PLAYER = 10
SALTO = 20
FRAME_RATE_PLAYER = 100
MOVE_RATE_PLAYER = 20
ALTURA_SALTO = 100



##########     DATOS GENERALES NIVELES     ##########
#ENEMIGOS
GRAVITY = 8
FRAME_RATE_MS = 10
MOVE_RATE_MS = 20
VIDAS = 3
#TAMAÑO PUERTA
TAMAÑO_PUERTA = 100,120

FPS = 30

###########     NIVEL UNO        ###########

#POSICION PLAYER
X = 20
Y_LVL1 = 550
#ENEMIGOS DATOS
SPEED_WALK = 3
#PUERTA
UBICACION_PUERTA_LVL1 = 1100, 120
#LLAVE
PUNTOS_LLAVE_LVL1 = 1300
X_LLAVE_LVL1 = 1070
Y_LLAVE_LVL1 = 180

##########       NIVEL DOS          ##########

#POSICION PLAYER
X = 20
Y_LVL2 = 100
#ENEMIGOS DATOS
SPEED_WALK1 = 1
SPEED_WALK2 = 2
#PUERTA
UBICACION_PUERTA_LVL2 = 1100, 600
# LLAVE
PUNTOS_LLAVE_LVL2 = 2000
X_LLAVE_LVL2 = 1080
Y_LLAVE_LVL2 = 650


##########        NIVEL TRES        ##########

#POSICION PLAYER
X = 20
Y_LVL3 = 550
#ENEMIGOS DATOS
X_BOSS = 800
Y_BOSS = 655
SPEED_WALKBOSS = 2
#PUERTA
UBICACION_PUERTA_LVL3 = 1200, 590
# LLAVE
X_LLAVE_LVL3 = 1180
Y_LLAVE_LVL3 = 650





teclas_letras = {
    pygame.K_a: "A",
    pygame.K_b: "B",
    pygame.K_c: "C",
    pygame.K_d: "D",
    pygame.K_e: "E",
    pygame.K_f: "F",
    pygame.K_g: "G",
    pygame.K_h: "H",
    pygame.K_i: "I",
    pygame.K_j: "J",
    pygame.K_k: "K",
    pygame.K_l: "L",
    pygame.K_m: "M",
    pygame.K_n: "N",
    pygame.K_o: "O",
    pygame.K_p: "P",
    pygame.K_q: "Q",
    pygame.K_r: "R",
    pygame.K_s: "S",
    pygame.K_t: "T",
    pygame.K_u: "U",
    pygame.K_v: "V",
    pygame.K_w: "W",
    pygame.K_x: "X",
    pygame.K_y: "Y",
    pygame.K_z: "Z",
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",
    pygame.K_8: "8",
    pygame.K_9: "9",
    pygame.K_0: "0"
}