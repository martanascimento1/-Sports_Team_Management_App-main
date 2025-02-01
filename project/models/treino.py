class Treino:
    def __init__(self, tipo, data, horario, duracao, local, profissional, realizado=False):
        self.tipo = tipo
        self.data = data
        self.horario = horario
        self.duracao = duracao
        self.local = local
        self.profissional = profissional
        self.realizado = realizado

    def marcar_como_realizado(self):
        self.realizado = True
        print("Treino realizado com sucesso.")

    def __str__(self):
        status = "Realizado" if self.realizado else "Agendado"
        return f"Tipo: {self.tipo}, Data: {self.data}, Horário: {self.horario}, Duração: {self.duracao} min\nLocal: {self.local}, Profissional: {self.profissional}, Status: {status}\n"