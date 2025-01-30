

perfis = []
inventario = []
lesoes = []


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

def monitorar_lesoes_saude ():
    atleta = input("Nome do atleta: "),
    idade = input ("Idade: "),
    grau = input ("Grau de risco de lesão: "),
    temp = input("Há quanto tempo esse atleta foi examinado?: "),
    res = input ("Resultado da última avaliação: "),
    est = input ("Estado atual de saúde: ")
    
    
    lesao = {
        "atleta": atleta,
        "idade": idade,
        "grau" : grau,
        "tempo" : temp,
        "resultado" : res,
        "estado_atual" : est
    }
    
    lesoes.append(lesao)
    

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

    print("\n Monitoramento de Saúde")
    for i, lesao in enumerate(lesoes, start=1):
        print(f"{i}. Atleta: {lesao['atleta']}, Idade: {lesao['idade']}, Grau de risco: {lesao['grau']}")
        print(f"   Último exame: {lesao['tempo']} atrás, Resultado: {lesao['resultado']}, Estado atual: {lesao['estado_atual']}\n")

        
        

def menu():
    while True:
        print("\n Gerenciamento da sua equipe")
        print("1. Cadastrar Perfil de Time")
        print("2. Listar Perfis")
        print("3. Cadastrar Objeto no Inventário")
        print("4. Listar Inventário")
        print("5. Monitorar Lesões")
        print("6. Mostrar Lesões")
        print("7. Sair")

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
            monitorar_lesoes_saude()
        elif opcao == "6":
            listar_lesoes_saude()
        elif opcao == "7":
            print("\nSaindo...\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()


