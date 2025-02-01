class Atleta:
    def __init__(self, nome, idade, funcao, participacoes_positivas=0, participacoes_negativas=0, erros_ultimas_partidas=0, acertos_ultimas_partidas=0):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.participacoes_positivas = participacoes_positivas
        self.participacoes_negativas = participacoes_negativas
        self.erros_ultimas_partidas = erros_ultimas_partidas
        self.acertos_ultimas_partidas = acertos_ultimas_partidas

    def atualizar_estatisticas(self, participacoes_positivas, participacoes_negativas, erros, acertos):
        self.participacoes_positivas += participacoes_positivas
        self.participacoes_negativas += participacoes_negativas
        self.erros_ultimas_partidas += erros
        self.acertos_ultimas_partidas += acertos
        print("Estatísticas do atleta atualizadas com sucesso.")

    def calcular_desempenho(self):
        desempenho = (self.acertos_ultimas_partidas - self.erros_ultimas_partidas) / (self.participacoes_positivas + self.participacoes_negativas) * 100
        return f"Desempenho: {desempenho:.2f}%"

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Função: {self.funcao}\nParticipações Positivas: {self.participacoes_positivas}, Participações Negativas: {self.participacoes_negativas}\nErros nas Últimas 2 Partidas: {self.erros_ultimas_partidas}, Acertos: {self.acertos_ultimas_partidas}\n"