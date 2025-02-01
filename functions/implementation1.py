

perfis = []
inventario = []
lesoes = []
agendamentos = []
treinos = []
jogadores = []
recrutamento = []

def cadastrar_perfil():
    name = input("Nome do Time: ")
    type_esporte = input("Tipo de Esporte: ")
    contact = input("Contato: ")
    resp = input("Nome do responsável legal: ")

    perfil = {
        "name": name,
        "type": type_esporte,
        "contato": contact,
        "responsavel": resp
    }

    perfis.append(perfil)  
    print("\nPerfil cadastrado com sucesso!\n")


def gerenciar_inventario():
    type_object = input("Tipo de objeto: ")
    setor = input("Setor em que se encontra: ")
    eq = input("Equipe responsável: ")
    ano = input("Ano em que foi adquirido: ")

    objeto = {
        "object": type_object,
        "setor": setor,
        "equipe": eq,
        "ano": ano
    }

    inventario.append(objeto)  
    print("\nObjeto cadastrado no inventário com sucesso!\n")

def atualizar_lesoes_saude():
    atleta = input("Nome do atleta: ")
    idade = input("Idade: ")
    teve_lesao = input("O atleta teve alguma lesão recente? (sim/não): ").strip().lower()

    lesao = {
        "atleta": atleta,
        "idade": idade,
        "teve_lesao": teve_lesao,
        "tipo_lesao": "Nenhuma",
        "grau": "Nenhum",
        "tratamento": "Nenhum",
        "tempo_recuperacao": "Não aplicável",
        "tempo_exame": "Não aplicável",
        "resultado": "Não aplicável",
        "estado_atual": "Saudável",
        "exames": "exames"
        
    }

    if teve_lesao == "sim":
        lesao["tipo_lesao"] = input("Qual foi o tipo da lesão? ")
        lesao["grau"] = input("Qual foi o grau da lesão? ")
        lesao["tratamento"] = input("Qual tratamento será realizadp? ")
        lesao["tempo_recuperacao"] = input("Qual o tempo estimado de recuperação? ")
        lesao["estado_atual"] = input("Estado atual de saúde: ")
    else:
        lesao["tempo_exame"] = input("Há quanto tempo esse atleta foi examinado? ")
        lesao["resultado"] = input("Resultado da última avaliação: ")
        lesao["estado_atual"] = input("Qual o estado atual de saúde após exames: ")
        lesao["exames"] = input("Quais os exames realizados agora? ")


    lesoes.append(lesao)
    listar_lesoes_saude()
    
def agendar_partida():
    tipo = input("O que deseja agendar? (partida/torneio): ").strip().lower()
    local = input("Local do evento: ")
    data = input("Data da partida/torneio (DD/MM/AAAA): ")
    horario = input("Horário do evento (HH:MM): ")
    adversario = input("Adversário ou equipes participantes: ")

    agendamento = {
        "tipo": tipo,
        "local": local,
        "data": data,
        "horario": horario,
        "adversario": adversario
    }

    agendamentos.append(agendamento)  
    print("\nAgendamento realizado com sucesso!\n")

    
    listar_agendamentos()
    
def agendar_treino():
    tipo = input("Tipo de treino: ")
    data = input("Data do treino (DD/MM/AAAA): ")
    horario = input("Horário de início (HH:MM): ")
    duracao = input("Duração estimada (em minutos): ")
    local = input("Local do treinamento: ")
    profissional = input("Profissional responsável: ")

    treino = {
        "tipo": tipo,
        "data": data,
        "horario": horario,
        "duracao": duracao,
        "local": local,
        "profissional": profissional,
        "realizado": False  
    }

    treinos.append(treino)
    print("\nTreinamento agendado com sucesso!\n")

    listar_treinos()

def registrar_treino_realizado():
    listar_treinos()
    
    if not treinos:
        return

    numero = int(input("Digite o número do treino realizado: ")) - 1

    if 0 <= numero < len(treinos):
        treinos[numero]["realizado"] = True
        print("\nTreino registrado como realizado com sucesso!\n")
    else:
        print("\nNúmero inválido. Tente novamente.\n")


def cadastrar_jogador():
    nome = input("Nome do jogador: ")
    idade = input("Idade: ")
    funcao = input("Função (posição do jogador): ")
    
    jogador = {
        "nome": nome,
        "idade": idade,
        "funcao": funcao,
        "participacoes_positivas": 0,
        "participacoes_negativas": 0,
        "erros_ultimas_partidas": 0,
        "acertos_ultimas_partidas": 0
    }

    jogadores.append(jogador)
    print("\nJogador cadastrado com sucesso!\n")

    listar_jogadores()
    
def cadastrar_jogador_recrutamento():
    nome = input("Nome do atleta: ")
    disponibilidade = input("Está disponível para contratação? (sim/não): ").strip().lower()
    idade = input("Idade: ")
    altura = input("Altura (em metros): ")
    peso = input("Peso (em kg): ")
    funcao = input("Função (posição do jogador): ")
    historico_lesoes = input("Possui histórico de lesões? (sim/não): ").strip().lower()
    titulos_importantes = input("Ganhou títulos importantes? (sim/não): ").strip().lower()
    bom_desempenho = input("Teve bom desempenho em equipes anteriores ou categorias de base? (sim/não): ").strip().lower()

    jogador = {
        "nome": nome,
        "disponivel": disponibilidade,
        "idade": idade,
        "altura": altura,
        "peso": peso,
        "funcao": funcao,
        "historico_lesoes": historico_lesoes,
        "titulos_importantes": titulos_importantes,
        "bom_desempenho": bom_desempenho
    }

    recrutamento.append(jogador)
    print("\nJogador cadastrado no processo de recrutamento com sucesso!\n")

    listar_jogadores_recrutamento()

    
def listar_treinos():
    if not treinos:
        print("\nNenhum treino agendado.\n")
        return

    print("\n Cronograma de Treinamentos ")
    for i, treino in enumerate(treinos, start=1):
        status = "Realizado" if treino["realizado"] else "Agendado"
        print(f"{i}. Tipo: {treino['tipo']}, Data: {treino['data']}, Horário: {treino['horario']}, Duração: {treino['duracao']} min")
        print(f"   Local: {treino['local']}, Profissional: {treino['profissional']}, Status: {status}\n")


def listar_perfis():
    if not perfis:
        print("\nNenhum perfil cadastrado.\n")
        return
    
    print("\nPerfis Cadastrados")
    for i, perfil in enumerate(perfis, start=1):
        print(f"{i}. {perfil['name']} - {perfil['type']} (Responsável: {perfil['responsavel']})")


def listar_inventario():
    if not inventario:
        print("\nNenhum objeto no inventário.\n")
        return

    print("\nInventário")
    for i, obj in enumerate(inventario, start=1):
        print(f"{i}. {obj['object']} - {obj['setor']} (Equipe: {obj['equipe']}, Ano: {obj['ano']})")

def listar_lesoes_saude():
    if not lesoes:
        print("\nNenhum registro de saúde cadastrado.\n")
        return

    print("\n Monitoramento de Lesões e Saúde ")
    for i, lesao in enumerate(lesoes, start=1):
        print(f"{i}. Atleta: {lesao['atleta']}, Idade: {lesao['idade']}, Teve lesão: {lesao['teve_lesao']}")
        
        if lesao["teve_lesao"] == "sim":
            print(f"   Tipo: {lesao['tipo_lesao']}, Grau: {lesao['grau']}, Tratamento: {lesao['tratamento']}")
            print(f"   Tempo estimado de recuperação: {lesao['tempo_recuperacao']}, Estado atual: {lesao['estado_atual']}\n")
        else:
            print(f"   Último exame: {lesao['tempo_exame']} atrás, Resultado: {lesao['resultado']}\n")
        
def listar_agendamentos():
    if not agendamentos:
        print("\nNenhuma partida ou torneio agendado.\n")
        return

    print("\n Agendamentos de Partidas e Torneios")
    for i, agendamento in enumerate(agendamentos, start=1):
        print(f"{i}. Tipo: {agendamento['tipo'].capitalize()}, Local: {agendamento['local']}")
        print(f"   Data: {agendamento['data']}, Horário: {agendamento['horario']}, Adversário: {agendamento['adversario']}\n")
        
def listar_jogadores():
    if not jogadores:
        print("\nNenhum jogador cadastrado.\n")
        return

    print("\nEscalação da Equipe")
    for i, jogador in enumerate(jogadores, start=1):
        print(f"{i}. Nome: {jogador['nome']}, Idade: {jogador['idade']}, Função: {jogador['funcao']}")
        print(f"   Participações Positivas: {jogador['participacoes_positivas']}, Participações Negativas: {jogador['participacoes_negativas']}")
        print(f"   Erros nas Últimas 2 Partidas: {jogador['erros_ultimas_partidas']}, Acertos: {jogador['acertos_ultimas_partidas']}\n")
 
def atualizar_estatisticas():
    listar_jogadores()
    
    if not jogadores:
        return

    numero = int(input("Digite o número do jogador para atualizar as estatísticas: ")) - 1

    if 0 <= numero < len(jogadores):
        jogadores[numero]["participacoes_positivas"] += int(input("Quantidade de participações positivas: "))
        jogadores[numero]["participacoes_negativas"] += int(input("Quantidade de participações negativas: "))
        jogadores[numero]["erros_ultimas_partidas"] += int(input("Quantidade de erros nas últimas 2 partidas: "))
        jogadores[numero]["acertos_ultimas_partidas"] += int(input("Quantidade de acertos nas últimas 2 partidas: "))

        print("\nEstatísticas atualizadas com sucesso!\n")
        listar_jogadores()
    else:
        print("\nNúmero inválido. Tente novamente.\n")   
        
def listar_jogadores_recrutamento():
    if not recrutamento:
        print("\nNenhum jogador no processo de recrutamento.\n")
        return

    print("\nJogadores Observados para Recrutamento")
    for i, jogador in enumerate(recrutamento, start=1):
        status = "Disponível" if jogador["disponivel"] == "sim" else "Indisponível"
        print(f"{i}. Nome: {jogador['nome']}, Idade: {jogador['idade']}, Altura: {jogador['altura']}m, Peso: {jogador['peso']}kg")
        print(f"   Função: {jogador['funcao']}, Histórico de Lesões: {jogador['historico_lesoes'].capitalize()}, Títulos Importantes: {jogador['titulos_importantes'].capitalize()}")
        print(f"   Bom Desempenho Anterior: {jogador['bom_desempenho'].capitalize()}, Status: {status}\n")

    
def menu():
    while True:
        print("\n Gerenciamento da sua equipe")
        print("1. Cadastrar Perfil de Time")
        print("2. Listar Perfis")
        print("3. Cadastrar Objeto no Inventário")
        print("4. Listar Inventário")
        print("5. Atualizar quadro de Lesões")
        print("6. Verificar quadro de Lesões")
        print("7. Agendar Competição")
        print ("8. Verificar competições agendadas")
        print ("9. Agendar treino Adicionar treino realizado")
        print ("10. Adicionar treino realizado")
        print ("11. Consultar treinos")
        print ("12. Cadastrar jogador")
        print ("13. Atualizar estatíticas")
        print ("14. Verificar escalação")
        print ("15. Adicionar novo jogador na lista de possíveis contratações")
        print ("16. Consultar lista de contratações desejadas")
        print ("17. ")
        print ("18. ")
        print ("19. ")
        print ("21. ")
        print ("22. ")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_perfil()
        elif opcao == "2":
            listar_perfis()
        elif opcao == "3":
            gerenciar_inventario()
        elif opcao == "4":
            listar_inventario()
        elif opcao == "5":
            atualizar_lesoes_saude()
        elif opcao == "6":
            listar_lesoes_saude()
        elif opcao =="7" :
            agendar_partida()
        elif opcao =="8" :
            listar_agendamentos()
        elif opcao == "9":
            agendar_treino()
        elif opcao == "10":
            registrar_treino_realizado()
        elif opcao =="11":
            listar_treinos()
        elif opcao =="12":
            cadastrar_jogador()
        elif opcao =="13":
            atualizar_estatisticas()
        elif opcao =="14":
            listar_jogadores()
        elif opcao =="15":
            cadastrar_jogador_recrutamento()
        elif opcao =="16":
            listar_jogadores_recrutamento()
        elif opcao == "0":
            print("\nSaindo...\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()


