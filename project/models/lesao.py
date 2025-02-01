class Lesao:
    def __init__(self, atleta, idade, teve_lesao, tipo_lesao=None, grau=None, tratamento=None, tempo_recuperacao=None, estado_atual=None, tempo_exame=None, resultado=None, exames=None):
        self.atleta = atleta
        self.idade = idade
        self.teve_lesao = teve_lesao
        self.tipo_lesao = tipo_lesao
        self.grau = grau
        self.tratamento = tratamento
        self.tempo_recuperacao = tempo_recuperacao
        self.estado_atual = estado_atual
        self.tempo_exame = tempo_exame
        self.resultado = resultado
        self.exames = exames


    def __str__(self):
        if self.teve_lesao == "sim":
            return f"Atleta: {self.atleta}, Idade: {self.idade}, Teve lesão: {self.teve_lesao}\nTipo: {self.tipo_lesao}, Grau: {self.grau}, Tratamento: {self.tratamento}\nTempo estimado de recuperação: {self.tempo_recuperacao}, Estado atual: {self.estado_atual}\n"
        else:
            return f"Atleta: {self.atleta}, Idade: {self.idade}, Teve lesão: {self.teve_lesao}\nÚltimo exame: {self.tempo_exame} atrás, Resultado: {self.resultado}\n"