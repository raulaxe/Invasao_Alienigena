import pygame
from pygame.sprite import Sprite

class Nave(Sprite):

    def __init__(self, screen, setting):
        super().__init__()
        self.screen = screen
        self.setting = setting
        self.image = pygame.image.load("C:/Users/usuario/OneDrive/PROJETOS/pycharm/pythonProject/invasao_alienigena/images/"
                                       "navetrans.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        self.moving_left = False
        self.moving_right = False

        self.center = float(self.rect.centerx)

    def update_move(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.setting.velocidade_nave

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.setting.velocidade_nave

        self.rect.centerx = self.center


    def blit_nave(self):

        self.screen.blit(self.image, self.rect)

    def center_nave(self):
        self.center = self.screen_rect.centerx