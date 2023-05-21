import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, settings):

        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load(
            "C:/Users/usuario/Documents/MeusReporitorios/invasao_alienigena/images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def update(self):

        self.x += (self.settings.velocidade_alien *
                   self.settings.direcao_frota)
        self.rect.x = self.x

    def check_bordas(self):

        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        if self.rect.left <= screen_rect.left:
            return True
