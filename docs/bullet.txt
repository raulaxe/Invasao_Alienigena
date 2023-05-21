import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, screen, setting, nave):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, setting.largura_bullet, setting.altura_bullet)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top
        self.y = float(self.rect.y)
        self.cor_bullet = setting.cor_bullet
        self.velocidade_bullet = setting.velocidade_bullet

    def bullet_move(self):

        self.y -= self.velocidade_bullet
        self.rect.y = self.y

    def draw_bullet(self):

        pygame.draw.rect(self.screen, self.cor_bullet, self.rect)
