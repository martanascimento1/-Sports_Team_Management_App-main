class Agendamento:
    def __init__(self, tipo, local, data, horario, adversario):
        self.tipo = tipo
        self.local = local
        self.data = data
        self.horario = horario
        self.adversario = adversario

    def verificar_status(self):
        from datetime import datetime
        data_evento = datetime.strptime(self.data, "%d/%m/%Y")
        if data_evento < datetime.now():
            return "Evento já ocorreu."
        return "Evento ainda não ocorreu."

    def __str__(self):
        return f"Tipo: {self.tipo.capitalize()}, Local: {self.local}\nData: {self.data}, Horário: {self.horario}, Adversário: {self.adversario}\n"