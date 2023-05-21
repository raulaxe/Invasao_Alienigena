class Setting():

    def __init__(self):

        self.largura_tela = 1200
        self.altura_tela = 800
        self.titulo_tela = " - INVASAO ALIENIGENA - "
        self.cor_tela = (240,240,240)

        self.velocidade_nave = 2.0

        self.largura_bullet = 3
        self.altura_bullet = 15
        self.cor_bullet = (60,60,60)
        self.velocidade_bullet = 3.0
        self.quantidade_bullets = 5

        self.velocidade_alien = 1.0
        self.frota_drop_speed = 10
        self.direcao_frota = 1
        self.limite_nave = 3
        self.taxa_velocidade = 1.1
        self.taxa_pontuacao = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.velocidade_nave = 1.5
        self.velocidade_bullet = 3
        self.velocidade_alien = 1
        self.direcao_frota = 1
        self.alien_points = 50

    def increase_speed(self):

        self.velocidade_nave *= self.taxa_velocidade
        self.velocidade_bullet *= self.taxa_velocidade
        self.velocidade_alien *= self.taxa_velocidade
        self.taxa_pontuacao = int(self.alien_points * self.taxa_pontuacao)


