class Financas:
    def __init__(self, montante, orcamento, gastos_atletas, gastos_funcionarios, outras_despesas, faturamento_mensal, faturamento_semestre, projecao_anual):
        self.montante = montante
        self.orcamento = orcamento
        self.gastos_atletas = gastos_atletas
        self.gastos_funcionarios = gastos_funcionarios
        self.outras_despesas = outras_despesas
        self.faturamento_mensal = faturamento_mensal
        self.faturamento_semestre = faturamento_semestre
        self.projecao_anual = projecao_anual

    def calcular_saldo(self):
        saldo = self.montante + self.faturamento_semestre - (self.gastos_atletas + self.gastos_funcionarios + self.outras_despesas)
        return f"Saldo disponível: R$ {saldo:.2f}"

    def verificar_orcamento(self):
        if self.gastos_atletas + self.gastos_funcionarios + self.outras_despesas > self.orcamento:
            return "Orçamento ultrapassado."
        return "Dentro do orçamento."

    def __str__(self):
        return f"Montante disponível: R$ {self.montante:.2f}\nOrçamento Semestral: R$ {self.orcamento:.2f}\nGastos com Atletas: R$ {self.gastos_atletas:.2f}\nGastos com Funcionários: R$ {self.gastos_funcionarios:.2f}\nOutras Despesas: R$ {self.outras_despesas:.2f}\nFaturamento Mensal: R$ {self.faturamento_mensal:.2f}\nFaturamento Semestral: R$ {self.faturamento_semestre:.2f}\nProjeção Anual: R$ {self.projecao_anual:.2f}\n"