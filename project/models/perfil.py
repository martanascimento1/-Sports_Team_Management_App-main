class Perfil:
    def __init__(self, name, type_esporte, contact, responsavel):
        self.name = name
        self.type = type_esporte
        self.contact = contact
        self.responsavel = responsavel

    def atualizar_contato(self, novo_contato):
        self.contact = novo_contato
        print(f"Contato atualizado para: {self.contact}")

    def exibir_resumo(self):
        print(f"Perfil: {self.name} ({self.type})")
        print(f"Responsável: {self.responsavel}, Contato: {self.contact}")

    def __str__(self):
        return f"{self.name} - {self.type} (Responsável: {self.responsavel})"