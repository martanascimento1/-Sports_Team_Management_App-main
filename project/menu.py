from models.perfil import Perfil
from models.inventario import Inventario
from models.lesao import Lesao
from models.agendamento import Agendamento
from models.treino import Treino
from models.atleta import Jogador
from models.recrutamento import Recrutamento
from models.desempenho import DesempenhoJogador, DesempenhoEquipe
from models.financas import Financas

class Gerenciador:
    def __init__(self):
        self.perfis = []
        self.inventario = []
        self.lesoes = []
        self.agendamentos = []
        self.treinos = []
        self.jogadores = []
        self.recrutamento = []
        self.desempenho_jogadores = []
        self.desempenho_equipe = []
        self.financas = []

    def menu(self):
        while True:
            print("\n Bem vindo ao gerenciamento da sua equipe esportiva ")
            print("1. Cadastrar Perfil de Time")
            print("2. Listar Perfis")
            print("3. Cadastrar Objeto no Inventário")
            print("4. Listar Inventário")
            print("5. Atualizar quadro de Lesões")
            print("6. Verificar quadro de Lesões")
            print("7. Agendar Competição")
            print("8. Verificar competições agendadas")
            print("9. Agendar treino")
            print("10. Adicionar treino realizado")
            print("11. Consultar treinos")
            print("12. Cadastrar jogador")
            print("13. Atualizar estatísticas")
            print("14. Verificar escalação")
            print("15. Adicionar novo jogador na lista de possíveis contratações")
            print("16. Consultar lista de contratações desejadas")
            print("17. Cadastrar desempenho da equipe")
            print("18. Cadastrar desempenho de atleta")
            print("19. Atualizar desempenho da equipe")
            print("20. Atualizar desempenho de atleta")
            print("21. Observar desempenho de atleta")
            print("22. Observar desempenho da equipe")
            print("23. Cadastrar dados financeiros")
            print("24. Atualizar dados financeiros")
            print("25. Observar finanças")
            print("26. Resumo financeiro geral")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_perfil()
            elif opcao == "2":
                self.listar_perfis()
            # ... (implementar outras opções)
            elif opcao == "0":
                print("\nSaindo...\n")
                break