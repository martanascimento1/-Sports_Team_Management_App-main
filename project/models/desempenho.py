class DesempenhoJogador:
    def __init__(self, nome, funcao, melhora, penalizacoes):
        self.nome = nome
        self.funcao = funcao
        self.melhora = melhora
        self.penalizacoes = penalizacoes

    def atualizar_penalizacoes(self, novas_penalizacoes):
        self.penalizacoes = novas_penalizacoes

    def avaliar_melhora(self):
        return "Houve melhora." if self.melhora == "sim" else "Não houve melhora."

    def __str__(self):
        return f"Nome: {self.nome}, Função: {self.funcao}\nHouve Melhora: {self.melhora.capitalize()}, Penalizações: {self.penalizacoes}\n"
    
class DesempenhoEquipe:
    def __init__(self, ganhos, pontos_positivos, pontos_negativos, setor_maior, setor_menor):
        self.ganhos = ganhos
        self.pontos_positivos = pontos_positivos
        self.pontos_negativos = pontos_negativos
        self.setor_maior = setor_maior
        self.setor_menor = setor_menor

    def analisar_ganhos(self):
        return f"Ganhos {self.ganhos}."

    def identificar_pontos_fortes(self):
        return f"Pontos fortes: {self.pontos_positivos}."

    def __str__(self):
        return f"Ganhos: {self.ganhos}\nPontos Positivos: {self.pontos_positivos}\nPontos Negativos: {self.pontos_negativos}\nSetores com Maior Desempenho: {self.setor_maior}\nSetores com Menor Desempenho: {self.setor_menor}\n"