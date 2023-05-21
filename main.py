import pygame
from settings import Setting
import game_functions as gf
from ship import Nave
from pygame.sprite import Group
from gamestats import Gamestats
from scoreboard import Scoreboard
from button import Button


def run_game():

    pygame.init()
    settings = Setting()
    screen = pygame.display.set_mode(
        (settings.largura_tela, settings.altura_tela))
    pygame.display.set_caption(settings.titulo_tela)
    button_play = Button(screen, settings, "Jogar")
    stats = Gamestats(settings)
    sb = Scoreboard(screen, settings, stats)
    nave = Nave(screen, settings)
    bullets = Group()
    aliens = Group()
    gf.criar_frota(screen, settings, nave, aliens)

    while True:

        gf.check_events(screen, stats, settings, nave,
                        aliens, bullets, button_play, sb)
        if stats.game_ativo == True:
            nave.update_move()
            gf.update_bullets(screen, settings, nave,
                              aliens, bullets, stats, sb)
            gf.update_aliens(screen, stats, settings,
                             nave, aliens, bullets, sb)

        gf.update_screen(screen, stats, settings, nave,
                         aliens, bullets, button_play, sb)


run_game()
