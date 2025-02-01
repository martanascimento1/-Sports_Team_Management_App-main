class Inventario:
    def __init__(self, type_object, setor, equipe, ano):
        self.type_object = type_object
        self.setor = setor
        self.equipe = equipe
        self.ano = ano

    def __str__(self):
        return f"{self.type_object} - {self.setor} (Equipe: {self.equipe}, Ano: {self.ano})"