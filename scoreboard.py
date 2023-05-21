import pygame.font
from pygame.sprite import Group
from ship import Nave


class Scoreboard():

    def __init__(self, screen, settings, stats):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_pont_maxima()
        self.prep_level()
        self.prep_naves()

    def prep_naves(self):
        self.naves = Group()
        for numero_nave in range(self.stats.naves_reservas):
            nave = Nave(self.screen, self.settings)
            nave.rect.x = 10 + (numero_nave * nave.rect.width)
            nave.rect.y = 10
            self.naves.add(nave)


    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.cor_tela)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_pont_maxima(self):
        pont_maxima = int(round(self.stats.pontuacao_maxima, -1))
        pont_maxima_str = "{:,}".format(pont_maxima)
        self.pont_maxima_image = self.font.render(pont_maxima_str, True, self.text_color, self.settings.cor_tela)
        self.pont_maxima_rect = self.pont_maxima_image.get_rect()
        self.pont_maxima_rect.centerx = self.screen_rect.centerx
        self.pont_maxima_rect.top = self.score_rect.top

    def prep_score(self):
        self.arredondamento = int(round(self.stats.score, -1))
        score_str = "{:,}".format(self.arredondamento)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.cor_tela)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.pont_maxima_image, self.pont_maxima_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.naves.draw(self.screen)