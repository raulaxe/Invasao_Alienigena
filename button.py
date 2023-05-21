import pygame.font


class Button():

    def __init__(self, screen, settings, msg):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.largura = 200
        self.altura = 50
        self.cor_botao = (0,255,0)
        self.cor_text = (255,255,255)
        self.fonte = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0,0, self.largura, self.altura)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)


    def prep_msg(self, msg):
        self.msg_image = self.fonte.render(msg, True, self.cor_text, self.cor_botao)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.cor_botao, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



