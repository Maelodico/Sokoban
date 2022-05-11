import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            "down" : self.get_image(65, 0),
            "left" : self.get_image(65, 185),
            "right" : self.get_image(65, 66),
            "up" : self.get_image(65, 125),
        }

    def change_animation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey((0, 0, 0))

    def move_right(self):
        self.position[0] += 3

    def move_left(self):
        self.position[0] -= 3

    def move_up(self):
        self.position[1] -= 3

    def move_down(self):
        self.position[1] += 3

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([50, 50])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 50, 50))
        return image