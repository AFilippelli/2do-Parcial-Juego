import pygame
import sys
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from nivel_tres import NivelTres
from leaderboard import *
from puntajes import *

screen = (1300,800)

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 45)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.DARK_GRAY = (30, 30, 30)
        self.LIGHT_GRAY = (200, 200, 200)
        self.HOVER_GRAY = (150, 150, 150)

        self.button_color_play = self.LIGHT_GRAY  # Color base de los botones
        self.button_color_options = self.LIGHT_GRAY
        self.button_color_exit = self.LIGHT_GRAY
        self.button_color_level1 = self.LIGHT_GRAY
        self.button_color_level2 = self.LIGHT_GRAY
        self.button_color_level3 = self.LIGHT_GRAY 
        self.button_color_back = self.LIGHT_GRAY

        self.level_one_completed = False
        self.level_two_completed = False
        self.level_three_completed = False
        self.level_music = None
        self.current_level = None

        self.background_image = pygame.image.load("imagenes/fondo_menu/castlevania_fondo.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.text_color_main_menu = (200, 200, 200)
        self.menu_music = pygame.mixer.Sound("sonidos/cancion menu/Castlevania II Music (NES) - Bloody Tears (Day Theme).mp3")  # Ruta de tu canción del menú
        self.menu_music.set_volume(0.2)  # Ajusta el volumen según sea necesario
        self.menu_music.play(-1)  # Reproduce la música en bucle

    def draw_text(self, text, color, x, y):
        text_obj = self.font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)

    def main_menu(self):
        while True:
            self.screen.blit(self.background_image,(0,0))

            # Botones
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_play = pygame.Rect(300, 200, 200, 50)
            button_options = pygame.Rect(300, 300, 200, 50)
            button_exit = pygame.Rect(300, 400, 200, 50)
            button_leaderboard = pygame.Rect(300, 500, 200, 50)  # Definir un nuevo botón
            main_menu_text = pygame.Rect(265,90,250,50)


            pygame.draw.rect(self.screen, self.button_color_play, button_play)
            self.draw_text('Jugar', self.BLACK, 350, 210)
            pygame.draw.rect(self.screen, self.button_color_options, button_options)
            self.draw_text('Opciones', self.BLACK, 330, 310)
            pygame.draw.rect(self.screen, self.button_color_exit, button_exit)
            self.draw_text('Salir', self.BLACK, 350, 410)
            pygame.draw.rect(self.screen, self.button_color_back, button_leaderboard)
            self.draw_text('Leaderboard', self.BLACK, 310, 510)  # Mostrar texto del botón
            pygame.draw.rect(self.screen,self.button_color_back,main_menu_text)
            self.draw_text('Menú Principal', "red", 280, 100)


            if button_play.collidepoint(mouse_x, mouse_y):
                self.button_color_play = self.HOVER_GRAY  # Cambia el color al pasar el mouse
            else:
                self.button_color_play = self.LIGHT_GRAY

            if button_options.collidepoint(mouse_x, mouse_y):
                self.button_color_options = self.HOVER_GRAY
            else:
                self.button_color_options = self.LIGHT_GRAY

            if button_exit.collidepoint(mouse_x, mouse_y):
                self.button_color_exit = self.HOVER_GRAY
            else:
                self.button_color_exit = self.LIGHT_GRAY

            if button_leaderboard.collidepoint(mouse_x, mouse_y):
                self.button_color_back = self.HOVER_GRAY
            else:
                self.button_color_back = self.LIGHT_GRAY

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_play.collidepoint(mouse_x, mouse_y):
                        self.game_options()
                    elif button_options.collidepoint(mouse_x, mouse_y):
                        self.game_info()
                    elif button_exit.collidepoint(mouse_x, mouse_y):
                        pygame.quit()
                        sys.exit()
                    elif button_leaderboard.collidepoint(mouse_x, mouse_y):
                            leaderbord(screen)  # Llama a la función leaderboard
            
            pygame.display.update()
            self.clock.tick()

    def game_options(self):
        while True:
            self.screen.blit(self.background_image,(0,0))

            mouse_x, mouse_y = pygame.mouse.get_pos()

            button_level1 = pygame.Rect(300, 200, 200, 50)
            button_level2 = pygame.Rect(300, 300, 200, 50)
            button_level3 = pygame.Rect(300, 400, 200, 50)
            back_button = pygame.Rect(50, 50, 120, 50)
            selec_level_text= pygame.Rect(190,90,315,50)

            pygame.draw.rect(self.screen, self.button_color_level1, button_level1)
            self.draw_text('Nivel 1', self.BLACK, 350, 210)
            pygame.draw.rect(self.screen, self.button_color_level2, button_level2)
            self.draw_text('Nivel 2', self.BLACK, 350, 310)
            pygame.draw.rect(self.screen, self.button_color_level3, button_level3)
            self.draw_text('Nivel 3', self.BLACK, 350, 410)
            pygame.draw.rect(self.screen, self.button_color_back, back_button)
            self.draw_text('Volver', self.BLACK, 60, 60)
            pygame.draw.rect(self.screen,self.button_color_back,selec_level_text)
            self.draw_text('Selecciona un Nivel', "red", 200, 100)


            if back_button.collidepoint(mouse_x, mouse_y):
                self.button_color_exit = self.HOVER_GRAY
            else:
                self.button_color_exit = self.LIGHT_GRAY

            if button_level1.collidepoint(mouse_x, mouse_y):
                self.button_color_level1 = self.HOVER_GRAY
            else:
                self.button_color_level1 = self.LIGHT_GRAY

            if button_level2.collidepoint(mouse_x, mouse_y):
                self.button_color_level2 = self.HOVER_GRAY
            else:
                self.button_color_level2 = self.LIGHT_GRAY

            if button_level3.collidepoint(mouse_x, mouse_y):
                self.button_color_level3 = self.HOVER_GRAY
            else:
                self.button_color_level3 = self.LIGHT_GRAY

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_level1.collidepoint(mouse_x, mouse_y):
                        self.start_level(NivelUno())
                    elif button_level2.collidepoint(mouse_x, mouse_y):
                        # Inicia el nivel 2 directamente, pero pasa el puntaje del nivel 1
                        self.current_level = NivelDos(0)  # Puedes pasar cualquier puntaje inicial aquí
                        self.start_level(self.current_level)
                    elif button_level3.collidepoint(mouse_x, mouse_y):
                        # Inicia el nivel 3 directamente, pasa el puntaje del nivel 2
                        self.current_level = NivelTres(0)  # Puedes pasar cualquier puntaje inicial aquí
                        self.start_level(self.current_level)
                    elif back_button.collidepoint(mouse_x, mouse_y):
                        return

            pygame.display.update()
            self.clock.tick(30)


    def game_info(self):
        while True:
            self.screen.fill(self.BLACK)  # Fondo negro
            # Texto explicativo sobre el funcionamiento del juego
            instructions = [
                "Bienvenido a mi juego, la tematica del mismo es plataformas. Tu objetivo es juntar la mayor cantidad de monedas posibles",
                "y perder la menor cantidad de vida que puedas, para asi conseguir el puntaje mas alto. Al terminar el ultimo nivel podrás",
                "guardar tu puntaje, y si tenes suerte, tendrás el mejor puntaje de todos",
                "Controles:",
                "Flecha izquiera: caminar iquierda",
                "Flecha derecha: caminar derecha",
                "Flecha arriba: saltar",
                "Espacio: saltar",
                "Z: atacar",
                "Shigt izquiero: correr",
                "Instrucción 3...",

            ]
            # Dibujar el texto en pantalla
            text_y = 50
            smaller_font = pygame.font.Font(None, 25)  # Definir una fuente más pequeña
            for line in instructions:
                text_obj = smaller_font.render(line, True, self.WHITE)
                text_rect = text_obj.get_rect()
                text_rect.topleft = (50, text_y)
                self.screen.blit(text_obj, text_rect)
                text_y += 30  # Espacio vertical entre líneas de texto
                # Botón para volver al menú principal
                back_button = pygame.Rect(50, 500, 120, 50)
                pygame.draw.rect(self.screen, self.HOVER_GRAY, back_button)
                self.draw_text('Volver', self.BLACK, 60, 510)

            # Lógica de botón y eventos
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if back_button.collidepoint(mouse_x, mouse_y):
                self.button_color_back = self.HOVER_GRAY
            else:
                self.button_color_back = self.LIGHT_GRAY

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(mouse_x, mouse_y):
                        return  # Volver al menú principal

            pygame.display.update()
            self.clock.tick(30)

    def start_level(self, level):
        self.current_level = level
        in_level = True
        while in_level:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        in_level = False  # Salir del bucle del nivel


            keys = pygame.key.get_pressed()
            delta_ms = self.clock.tick(30)

            #ejecuta el nivel actual
            level.run_level(level.screen, keys, delta_ms, level.player_1)

            if level.level_completed:
                if isinstance(level, NivelUno):  # Si es el nivel uno, inicia el nivel dos
                    self.level_one_completed = True  # Inicia el nivel dos
                    self.start_level(NivelDos(self.current_level.player_1.score))
                if isinstance(level, NivelDos):  
                    self.level_two_completed = True  
                    self.start_level(NivelTres(self.current_level.player_1.score))
                if isinstance(level, NivelTres):  
                    self.level_three_completed = True 
                    print(type(self.current_level.player_1.score))
                    retorno = mostrar_puntajes(self.current_level.player_1.score,screen)
                    if retorno == True:

                        self.main_menu()


            pygame.display.flip()

        # Volver al menú principal
        self.main_menu()  # Llama de nuevo al menú principal cuando se sale del nivel


if __name__ == '__main__':
    pygame.init()
    menu = Menu(screen)
    menu.main_menu()