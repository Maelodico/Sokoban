import pygame
import pytmx
import pyscroll

from Sokoban.player import Player


class Game:

    def __init__(self):
        # on créer la fenêtre de jeu

        self.screen = pygame.display.set_mode((950, 950))
        pygame.display.set_caption("SOKOBAN - Adventure")


        # charger la carte

        tmx_data = pytmx.util_pygame.load_pygame("cartes.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        # generer un joueur
        player_position = tmx_data.get_object_by_name("Player")
        self.player = Player(player_position.x, player_position.y)

        # generer les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == 'collision':
                print("collision")
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calque (eau, chemain,...)
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')


    def run(self):

        #clock = pygame.time.Clock()

        # boucle de jeu

        running = True

        while running:

            self.handle_input()
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # temps de tour de boucle
            #clock.tick(90)

        pygame.quit()

