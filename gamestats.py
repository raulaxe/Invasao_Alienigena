
class Gamestats():
    def __init__(self, settings):

        self.settings = settings
        self.reset_stats()
        self.game_ativo = False
        self.pontuacao_maxima = 0


    def reset_stats(self):
        self.naves_reservas = self.settings.limite_nave
        self.score = 0
        self.level = 1
