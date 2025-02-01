from models.perfil import Perfil
from models.inventario import Inventario
from models.lesao import Lesao
from models.agendamento import Agendamento
from models.treino import Treino
from models.atleta import Atleta
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
          print("\n Gerenciamento da sua equipe")
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
          elif opcao == "3":
            self.gerenciar_inventario()
          elif opcao == "4":
            self.listar_inventario()
          elif opcao == "5":
            self.atualizar_lesoes_saude()
          elif opcao == "6":
            self.listar_lesoes_saude()
          elif opcao == "7":
            self.agendar_partida()
          elif opcao == "8":
            self.listar_agendamentos()
          elif opcao == "9":
            self.agendar_treino()
          elif opcao == "10":
            self.registrar_treino_realizado()
          elif opcao == "11":
            self.listar_treinos()
          elif opcao == "12":
            self.cadastrar_jogador()
          elif opcao == "13":
            self.atualizar_estatisticas()
          elif opcao == "14":
            self.listar_jogadores()
          elif opcao == "15":
            self.cadastrar_jogador_recrutamento()
          elif opcao == "16":
            self.listar_jogadores_recrutamento()
          elif opcao == "17":
            self.cadastrar_desempenho_equipe()
          elif opcao == "18":
            self.cadastrar_desempenho_jogador()
          elif opcao == "19":
            self.atualizar_desempenho_equipe()
          elif opcao == "20":
            self.atualizar_desempenho_jogador()
          elif opcao == "21":
            self.listar_desempenho_jogadores()
          elif opcao == "22":
            self.listar_desempenho_equipe()
          elif opcao == "23":
            self.cadastrar_financas()
          elif opcao == "24":
            self.atualizar_financas()
          elif opcao == "25":
            self.listar_financas()
          elif opcao == "26":
            self.resumo_financeiro()
          elif opcao == "0":
            print("\nSaindo...\n")
            break  # O break está dentro do loop while
          else:
            print("\nOpção inválida. Tente novamente.\n")   
            
        # Métodos para Perfil
    def cadastrar_perfil(self):
        name = input("Nome do Time: ")
        type_esporte = input("Tipo de Esporte: ")
        contact = input("Contato: ")
        responsavel = input("Nome do responsável legal: ")

        perfil = Perfil(name, type_esporte, contact, responsavel)
        self.perfis.append(perfil)
        print("\nPerfil cadastrado com sucesso!\n")

    def listar_perfis(self):
        if not self.perfis:
            print("\nNenhum perfil cadastrado.\n")
            return

        print("\nPerfis Cadastrados")
        for i, perfil in enumerate(self.perfis, start=1):
            print(f"{i}. {perfil}")

    # Métodos para Inventário
    def cadastrar_inventario(self):
        type_object = input("Tipo de objeto: ")
        setor = input("Setor em que se encontra: ")
        equipe = input("Equipe responsável: ")
        ano = input("Ano em que foi adquirido: ")

        objeto = Inventario(type_object, setor, equipe, ano)
        self.inventario.append(objeto)
        print("\nObjeto cadastrado no inventário com sucesso!\n")

    def listar_inventario(self):
        if not self.inventario:
            print("\nNenhum objeto no inventário.\n")
            return

        print("\nInventário")
        for i, obj in enumerate(self.inventario, start=1):
            print(f"{i}. {obj}")

    # Métodos para Lesões
    def atualizar_lesoes_saude(self):
        atleta = input("Nome do atleta: ")
        idade = input("Idade: ")
        teve_lesao = input("O atleta teve alguma lesão recente? (sim/não): ").strip().lower()

        if teve_lesao == "sim":
            tipo_lesao = input("Qual foi o tipo da lesão? ")
            grau = input("Qual foi o grau da lesão? ")
            tratamento = input("Qual tratamento será realizado? ")
            tempo_recuperacao = input("Qual o tempo estimado de recuperação? ")
            estado_atual = input("Estado atual de saúde: ")
            lesao = Lesao(atleta, idade, teve_lesao, tipo_lesao, grau, tratamento, tempo_recuperacao, estado_atual)
        else:
            tempo_exame = input("Há quanto tempo esse atleta foi examinado? ")
            resultado = input("Resultado da última avaliação: ")
            estado_atual = input("Qual o estado atual de saúde após exames: ")
            exames = input("Quais os exames realizados agora? ")
            lesao = Lesao(atleta, idade, teve_lesao, tempo_exame=tempo_exame, resultado=resultado, estado_atual=estado_atual, exames=exames)

        self.lesoes.append(lesao)
        print("\nRegistro de saúde atualizado com sucesso!\n")

    def listar_lesoes_saude(self):
        if not self.lesoes:
            print("\nNenhum registro de saúde cadastrado.\n")
            return

        print("\n Monitoramento de Lesões e Saúde ")
        for i, lesao in enumerate(self.lesoes, start=1):
            print(f"{i}. {lesao}")

    # Métodos para Agendamento
    def agendar_partida(self):
        tipo = input("O que deseja agendar? (partida/torneio): ").strip().lower()
        local = input("Local do evento: ")
        data = input("Data da partida/torneio (DD/MM/AAAA): ")
        horario = input("Horário do evento (HH:MM): ")
        adversario = input("Adversário ou equipes participantes: ")

        agendamento = Agendamento(tipo, local, data, horario, adversario)
        self.agendamentos.append(agendamento)
        print("\nAgendamento realizado com sucesso!\n")

    def listar_agendamentos(self):
        if not self.agendamentos:
            print("\nNenhuma partida ou torneio agendado.\n")
            return

        print("\n Agendamentos de Partidas e Torneios")
        for i, agendamento in enumerate(self.agendamentos, start=1):
            print(f"{i}. {agendamento}")

    # Métodos para Treino
    def agendar_treino(self):
        tipo = input("Tipo de treino: ")
        data = input("Data do treino (DD/MM/AAAA): ")
        horario = input("Horário de início (HH:MM): ")
        duracao = input("Duração estimada (em minutos): ")
        local = input("Local do treinamento: ")
        profissional = input("Profissional responsável: ")

        treino = Treino(tipo, data, horario, duracao, local, profissional)
        self.treinos.append(treino)
        print("\nTreinamento agendado com sucesso!\n")

    def listar_treinos(self):
        if not self.treinos:
            print("\nNenhum treino agendado.\n")
            return

        print("\n Cronograma de Treinamentos ")
        for i, treino in enumerate(self.treinos, start=1):
            print(f"{i}. {treino}")

    def registrar_treino_realizado(self):
        self.listar_treinos()

        if not self.treinos:
            return

        numero = int(input("Digite o número do treino realizado: ")) - 1

        if 0 <= numero < len(self.treinos):
            self.treinos[numero].realizado = True
            print("\nTreino registrado como realizado com sucesso!\n")
        else:
            print("\nNúmero inválido. Tente novamente.\n")

    # Métodos para Jogador
    def cadastrar_jogador(self):
        nome = input("Nome do jogador: ")
        idade = input("Idade: ")
        funcao = input("Função (posição do jogador): ")

        jogador = Jogador(nome, idade, funcao)
        self.jogadores.append(jogador)
        print("\nJogador cadastrado com sucesso!\n")

    def listar_jogadores(self):
        if not self.jogadores:
            print("\nNenhum jogador cadastrado.\n")
            return

        print("\nEscalação da Equipe")
        for i, jogador in enumerate(self.jogadores, start=1):
            print(f"{i}. {jogador}")

    def atualizar_estatisticas(self):
        self.listar_jogadores()

        if not self.jogadores:
            return

        numero = int(input("Digite o número do jogador para atualizar as estatísticas: ")) - 1

        if 0 <= numero < len(self.jogadores):
            self.jogadores[numero].participacoes_positivas += int(input("Quantidade de participações positivas: "))
            self.jogadores[numero].participacoes_negativas += int(input("Quantidade de participações negativas: "))
            self.jogadores[numero].erros_ultimas_partidas += int(input("Quantidade de erros nas últimas 2 partidas: "))
            self.jogadores[numero].acertos_ultimas_partidas += int(input("Quantidade de acertos nas últimas 2 partidas: "))

            print("\nEstatísticas atualizadas com sucesso!\n")
        else:
            print("\nNúmero inválido. Tente novamente.\n")

    # Métodos para Recrutamento
    def cadastrar_jogador_recrutamento(self):
        nome = input("Nome do atleta: ")
        disponibilidade = input("Está disponível para contratação? (sim/não): ").strip().lower()
        idade = input("Idade: ")
        altura = input("Altura (em metros): ")
        peso = input("Peso (em kg): ")
        funcao = input("Função (posição do jogador): ")
        historico_lesoes = input("Possui histórico de lesões? (sim/não): ").strip().lower()
        titulos_importantes = input("Ganhou títulos importantes? (sim/não): ").strip().lower()
        bom_desempenho = input("Teve bom desempenho em equipes anteriores ou categorias de base? (sim/não): ").strip().lower()

        jogador = Recrutamento(nome, disponibilidade, idade, altura, peso, funcao, historico_lesoes, titulos_importantes, bom_desempenho)
        self.recrutamento.append(jogador)
        print("\nJogador cadastrado no processo de recrutamento com sucesso!\n")

    def listar_jogadores_recrutamento(self):
        if not self.recrutamento:
            print("\nNenhum jogador no processo de recrutamento.\n")
            return

        print("\nJogadores Observados para Recrutamento")
        for i, jogador in enumerate(self.recrutamento, start=1):
            print(f"{i}. {jogador}")

    # Métodos para Desempenho
    def cadastrar_desempenho_equipe(self):
        ganhos = input("Os ganhos da equipe aumentaram ou diminuíram? ")
        pontos_positivos = input("Principais pontos positivos da equipe: ")
        pontos_negativos = input("Principais pontos negativos da equipe: ")
        setor_maior = input("Setores com maior desempenho: ")
        setor_menor = input("Setores com menor desempenho: ")

        desempenho = DesempenhoEquipe(ganhos, pontos_positivos, pontos_negativos, setor_maior, setor_menor)
        self.desempenho_equipe.append(desempenho)
        print("\nDesempenho da equipe registrado com sucesso!\n")

    def listar_desempenho_equipe(self):
        if not self.desempenho_equipe:
            print("\nNenhum desempenho da equipe registrado.\n")
            return

        print("\nAcompanhamento de Desempenho da Equipe")
        for i, desempenho in enumerate(self.desempenho_equipe, start=1):
            print(f"{i}. {desempenho}")

    def cadastrar_desempenho_jogador(self):
        nome = input("Nome do atleta: ")
        funcao = input("Função (posição do jogador): ")
        melhora = input("Houve melhora no desempenho? (sim/não): ").strip().lower()
        penalizacoes = input("O atleta sofreu penalizações? Se sim, quais? (ou digite 'nenhuma'): ")

        desempenho = DesempenhoJogador(nome, funcao, melhora, penalizacoes)
        self.desempenho_jogadores.append(desempenho)
        print("\nDesempenho do jogador registrado com sucesso!\n")

    def listar_desempenho_jogadores(self):
        if not self.desempenho_jogadores:
            print("\nNenhum desempenho de jogador registrado.\n")
            return

        print("\n Acompanhamento de Desempenho dos Jogadores")
        for i, desempenho in enumerate(self.desempenho_jogadores, start=1):
            print(f"{i}. {desempenho}")

    def cadastrar_financas(self):
        montante = float(input("Montante disponível (R$): "))
        orcamento = float(input("Orçamento planejado para o semestre (R$): "))
        gastos_atletas = float(input("Gastos com atletas (R$): "))
        gastos_funcionarios = float(input("Gastos com demais funcionários (R$): "))
        outras_despesas = float(input("Demais despesas (R$): "))
        faturamento_mensal = float(input("Faturamento mensal (R$): "))
        faturamento_semestre = float(input("Faturamento do último semestre (R$): "))
        projecao_anual = float(input("Projeção de faturamento para o ano (R$): "))

        financa = Financas(montante, orcamento, gastos_atletas, gastos_funcionarios, outras_despesas, faturamento_mensal, faturamento_semestre, projecao_anual)
        self.financas.append(financa)
        print("\nDados financeiros registrados com sucesso!\n")

    def listar_financas(self):
        if not self.financas:
            print("\nNenhum registro financeiro encontrado.\n")
            return

        print("\n Relatório Financeiro")
        for i, financa in enumerate(self.financas, start=1):
            print(f"{i}. {financa}")

    def resumo_financeiro(self):
        if not self.financas:
            print("\nNenhum dado financeiro registrado.\n")
            return

        financa = self.financas[-1]  # Pega o último registro financeiro inserido

        despesas_totais = financa.gastos_atletas + financa.gastos_funcionarios + financa.outras_despesas
        saldo_atual = financa.montante + financa.faturamento_semestre - despesas_totais

        print("\nResumo Financeiro")
        print(f"Saldo Atual: R$ {saldo_atual:.2f}")
        print(f"Despesas Totais: R$ {despesas_totais:.2f}")
        print(f"Faturamento Mensal: R$ {financa.faturamento_mensal:.2f}")
        print(f"Projeção Anual: R$ {financa.projecao_anual:.2f}\n")