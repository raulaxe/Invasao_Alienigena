import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from gamestats import Gamestats

# FUNÇÃO QUE VERIFICA TODOS OS EVENTOS DE TECLAS NA POSIÇÃO BAIXA:
def check_keydown(event, stats, screen, settings, nave, bullets):

    if event.key == pygame.K_LEFT:

        nave.moving_left = True

    if event.key == pygame.K_RIGHT:

        nave.moving_right = True

    if stats.game_ativo == True:

        if event.key == pygame.K_SPACE:

            fire_bullets(screen, settings, nave, bullets)

    if event.key == pygame.K_q:

        sys.exit()

# FUNÇÃO QUE VERIFICA TODOS OS EVENTOS DE TECLAS NA POSIÇÃO ALTA:
def check_keyup(event, nave):

    if event.key == pygame.K_LEFT:

        nave.moving_left = False

    if event.key == pygame.K_RIGHT:

        nave.moving_right = False

# FUNCAO QUE VERIFICA SE O BOTAO JOGAR FOI CLICADO E INICIA O JOGO, FAZENDO O MOUSE DESAPARECER DA TELA:
def check_play_button(screen, stats, settings, nave, aliens, bullets, button_play, mouse_x, mouse_y, sb):

    button_clicked = button_play.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_ativo:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_ativo = True
        sb.prep_score()
        sb.prep_pont_maxima()
        sb.prep_level()
        sb.prep_naves()
        aliens.empty()
        bullets.empty
        criar_frota(screen,settings, nave, aliens)
        nave.center_nave()

# FUNÇÃO QUE VERIFICA TODOS OS EVENTOS DO JOGO COMO OS MOVIMENTOS, CLIQUES E PRESSIONAMENTOS DE TECLAS:
def check_events(screen, stats, settings, nave, aliens, bullets, button_play, sb):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, stats, settings, nave, aliens, bullets, button_play, mouse_x, mouse_y, sb)

        if event.type == pygame.KEYDOWN:

            check_keydown(event, stats, screen, settings, nave, bullets)

        if event.type == pygame.KEYUP:

            check_keyup(event, nave)

# FUNÇÃO QUE ATUALIZA OS RECURSOS DE TELA:
def update_screen(screen, stats, settings, nave, aliens, bullets, button_play, sb):

    screen.fill(settings.cor_tela)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        bullet.bullet_move()

    nave.blit_nave()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_ativo:
        button_play.draw_button()
    pygame.display.flip()

# FUNÇÃO QUE MOVIMENTA E REMOVE OS PROJETEIS DA LISTA CRIADA:
def update_bullets(screen, settings, nave, aliens, bullets, stats, sb):

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_colisoes_bullet_alien(screen, settings, nave, aliens, bullets, stats, sb)

# FUNÇÃO QUE VERIFICA SE A FROTA DE ALIENS CHEGA AO BOTTOM DA TELA:
def check_aliens_bottom(screen, stats, settings, nave, aliens, bullets, sb):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            return True

# FUNÇÃO QUE APAGA O ALIEN QUE COLIDIR COM O PROJETIL AO SER DISPARADO:
def check_colisoes_bullet_alien(screen, settings, nave, aliens, bullets, stats, sb):

    colisoes = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if colisoes:
        stats.score += settings.alien_points
        sb.prep_score()
        check_pont_maxima(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        criar_frota(screen, settings, nave, aliens)

# FUNÇÃO QUE LIMITA A QUANTIDADE DE DISPAROS DA NAVE:
def fire_bullets(screen, settings, nave, bullets):

    if len(bullets) <= settings.quantidade_bullets:
        new_bullet = Bullet(screen, settings, nave)
        bullets.add(new_bullet)

# FUNÇÃO QUE CRIA A NOVA FROTA DE ALIENS:
def criar_frota(screen, settings, nave, aliens):

    alien = Alien(screen, settings)
    largura_alien = alien.rect.width
    altura_alien = alien.rect.height
    quant_aliens_linha = get_quant_aliens_x(settings, largura_alien)
    quant_linhas = get_quant_linhas(screen, settings, altura_alien,nave)

    for numero_linha in range(quant_linhas):
        for numero_alien in range(quant_aliens_linha):
            criar_alien(screen, settings, largura_alien, altura_alien, numero_alien,numero_linha, aliens)

# FUNÇÃO QUE VERIFICA A QUANTIDADE DE ALIENS POR LINHA:
def get_quant_aliens_x(settings, largura_alien):
    espaco_disp_x = settings.largura_tela - (2 * largura_alien)
    quant_aliens_x = int(espaco_disp_x / (2 * largura_alien))
    return quant_aliens_x

# FUNÇÃO QUE VERIFICA A QUANTIDADE DE LINHAS DE ALIENS:
def get_quant_linhas(screen, settings, altura_alien, nave):
    esp_disp_y = settings.altura_tela - (3 * altura_alien) - nave.rect.height
    quant_linhas_y = int(esp_disp_y / (2 * altura_alien))
    return quant_linhas_y

# FUNÇÃO QUE CRIA O ALIEN QUE SERA INCLUIDO NA FROTA:
def criar_alien(screen, settings, largura_alien, altura_alien, numero_alien,numero_linha, aliens):

    alien = Alien(screen, settings)
    alien.x = largura_alien + (2 * largura_alien) * (numero_alien)
    alien.rect.x = alien.x
    alien.y = altura_alien = (2 * altura_alien) * (numero_linha)
    alien.rect.y = alien.y
    aliens.add(alien)

# FUNÇÃO QUE VERIFICA A QUANTIDADE DE NAVES RESERVAS E REINICIA OS DADOS DO JOGO:
def nave_hit(screen, settings, nave, aliens, bullets, stats, sb):
    stats.naves_reservas -= 1

    if stats.naves_reservas > 0:
        sb.prep_naves()
        aliens.empty()
        bullets.empty()
        criar_frota(screen, settings, nave, aliens)
        nave.center_nave()
        sleep(0.5)


    else:
        pygame.mouse.set_visible(True)
        stats.game_ativo = False

# FUNCAO QUE VERIFICA TODOS OS MOVIMENTOS DO FROTA DE ALIENS:
def update_aliens(screen, stats, settings, nave, aliens, bullets, sb):
    checked_bottom = check_aliens_bottom(screen, stats, settings, nave, aliens, bullets, sb)
    check_bordas_frota(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(nave, aliens):
        nave_hit(screen, settings, nave, aliens, bullets, stats, sb)

    if checked_bottom == True:
        nave_hit(screen, settings, nave, aliens, bullets, stats, sb)

# FUNCAO QUE VERIFICA SE A FROTA DE ALIENS ALCANÇOU A BORDA DA TELA:
def check_bordas_frota(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_bordas():
            mudar_direcao_frota(settings, aliens)
            break

# FUNCAO QUE ALTERA O SENTIDO QUE A FROTA DE ALIENS SE MOVIMENTA:
def mudar_direcao_frota(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.frota_drop_speed
    settings.direcao_frota *= -1


def check_pont_maxima(stats, sb):
    if stats.score > stats.pontuacao_maxima:
        stats.pontuacao_maxima = stats.score
        sb.prep_pont_maxima()




