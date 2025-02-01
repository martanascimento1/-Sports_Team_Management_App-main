class Recrutamento:
    def __init__(self, nome, disponibilidade, idade, altura, peso, funcao, historico_lesoes, titulos_importantes, bom_desempenho):
        self.nome = nome
        self.disponibilidade = disponibilidade
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.funcao = funcao
        self.historico_lesoes = historico_lesoes
        self.titulos_importantes = titulos_importantes
        self.bom_desempenho = bom_desempenho

    def verificar_disponibilidade(self):
        return "Disponível" if self.disponibilidade == "sim" else "Indisponível"

    def avaliar_potencial(self):
        if self.titulos_importantes == "sim" and self.bom_desempenho == "sim":
            return "Alto potencial."
        return "Potencial moderado."

    def __str__(self):
        status = "Disponível" if self.disponibilidade == "sim" else "Indisponível"
        return f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}m, Peso: {self.peso}kg\nFunção: {self.funcao}, Histórico de Lesões: {self.historico_lesoes.capitalize()}, Títulos Importantes: {self.titulos_importantes.capitalize()}\nBom Desempenho Anterior: {self.bom_desempenho.capitalize()}, Status: {status}\n"