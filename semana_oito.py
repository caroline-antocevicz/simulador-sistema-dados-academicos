# Nome aluna: Caroline Oliveira Antocevicz
# Curso: Análise e desenvolvimento de sistemas

import json

# CRIAÇÃO DE FUNÇÕES

# FUNÇÃO MENU PRINCIPAL
def menu_principal():
    print('----- MENU PRINCIPAL -----\n')
    print('(1) Gerenciar estudantes.')
    print('(2) Gerenciar professores.')
    print('(3) Gerenciar disciplinas.')
    print('(4) Gerenciar turmas.')
    print('(5) Gerenciar matrículas.')
    print('(0) Sair.\n')

    return int(input('Informe o número que corresponde a opção desejada: '))

# FUNÇÃO VALIDA OPÇÃO MENU PRINCIPAL
def valida_opcao_menu_principal(opcao):
    if opcao == 1:
        opcao_menu = 'estudantes'
    elif opcao == 2:
        opcao_menu = 'professores'
    elif opcao == 3:
        opcao_menu = 'disciplinas'
    elif opcao == 4:
        opcao_menu = 'turmas'
    elif opcao == 5:
        opcao_menu = 'matrículas'
    
    return opcao_menu

# FUNÇÃO MENU DE OPERAÇÕES
def menu_operacoes(opcao):
    print('***** [{}] MENU DE OPERAÇÕES *****\n'.format(opcao.upper()))
    print('(1) Incluir.')
    print('(2) Listar.')
    print('(3) Atualizar.')
    print('(4) Excluir.')
    print('(9) Voltar ao menu principal.\n')

    return int(input('Informe o número que corresponde a opção desejada: '))

# FUNÇÃO INCLUSÃO CADASTRO
def inclusao_cadastro(opcao_menu_principal,nome_arquivo):
    print('===== INCLUSÃO =====\n')

    if opcao_menu_principal == 1:
        sujeito = valida_opcao_menu_principal(opcoes_menu_principal).rstrip('s')

        try:
            codigo = int(input(f'Informe o código do {sujeito} (ex: 1): '))
            nome = input(f'Informe o nome do {sujeito}: ')
            cpf = input(f'Informe o CPF do {sujeito}: ')
        except ValueError:
            print('Você informou um valor incorreto em uma das opções abaixo. Informe novamente\n')
            codigo = int(input(f'Informe o código do {sujeito} (ex: 1): '))
            nome = input(f'Informe o nome do {sujeito}: ')
            cpf = input(f'Informe o CPF do {sujeito}: ')
    
        cadastro = {
            "codigo": codigo,
            "nome": nome,
            "cpf": cpf
        }

        atualiza_arquivo(cadastro, nome_arquivo)

    elif opcao_menu_principal == 2:
        sujeito = valida_opcao_menu_principal(opcoes_menu_principal).rstrip('es')

        try:
            codigo = int(input(f'Informe o código do {sujeito} (ex: 1): '))
            nome = input(f'Informe o nome do {sujeito}: ')
            cpf = input(f'Informe o CPF do {sujeito}: ')
        except ValueError:
            print('Você informou um valor incorreto em uma das opções abaixo. Informe novamente\n')
            codigo = int(input(f'Informe o código do {sujeito} (ex: 1): '))
            nome = input(f'Informe o nome do {sujeito}: ')
            cpf = input(f'Informe o CPF do {sujeito}: ')
    
        cadastro = {
            "codigo": codigo,
            "nome": nome,
            "cpf": cpf
        }

        atualiza_arquivo(cadastro, nome_arquivo)

    elif opcao_menu_principal == 3:
        try:
            codigo = int(input('Informe o código da disciplina (ex: 01): '))
            nome = input('Informe o nome da disciplina (ex: 01): ')
        except ValueError:
            print('Você informou um valor incorreto em uma das opções abaixo. Informe novamente\n')
            codigo = int(input('Informe o código da disciplina (ex: 01): '))
            nome = input('Informe o nome da disciplina (ex: 01): ')

        cadastro = {
            "codigo": codigo,
            "nome": nome
        }
        
        atualiza_arquivo(cadastro, nome_arquivo)
    
    elif opcao_menu_principal == 4:
        codigo_turma = int(input('Informe o código da turma: '))
        codigo_professor = int(input('Informe o código do professor: '))
        codigo_disciplina = int(input('Informe o código da disciplina: '))

        lista = ler_arquivo(nome_arquivo)
        
        if len(lista) > 0:
            codigos_existentes = []
            for item in lista:
                codigos_existentes.append(item["codigo_turma"])

            if codigo_turma in codigos_existentes:
                print('Já existe uma turma com esse código')
            else:      
                cadastro = {
                    "codigo_turma": codigo_turma,
                    "codigo_professor": codigo_professor,
                    "codigo_disciplina": codigo_disciplina
                }

                atualiza_arquivo(cadastro, nome_arquivo)
                
        else:
            cadastro = {
                "codigo_turma": codigo_turma,
                "codigo_professor": codigo_professor,
                "codigo_disciplina": codigo_disciplina
            }
            
            atualiza_arquivo(cadastro, nome_arquivo)

    elif opcao_menu_principal == 5:
        codigo_matricula = int(input('Informe o código da matricula: '))
        codigo_estudante = int(input('Informe o código do estudante: '))

        lista = ler_arquivo(nome_arquivo)
        
        if len(lista) > 0:
            codigos_existentes = []
            for item in lista:
                codigos_existentes.append(item["codigo_matricula"])

            if codigo_matricula in codigos_existentes:
                print('Já existe uma matricula com esse código')
            else:      
                cadastro = {
                    "codigo_matricula": codigo_matricula,
                    "codigo_estudante": codigo_estudante
                }

                atualiza_arquivo(cadastro, nome_arquivo)
                
        else:
            cadastro = {
                "codigo_matricula": codigo_matricula,
                "codigo_estudante": codigo_estudante
            }
            
            atualiza_arquivo(cadastro, nome_arquivo)

    else:
        print('Opção inválida.\n')

    input('Pressione ENTER para continuar.\n') 

# FUNÇÃO LISTAR CADASTRO
def listar_cadastro(opcao, nome_arquivo):
    lista = ler_arquivo(nome_arquivo)

    print(f'Você escolheu a opção válida {opcao}.\n')
    print('===== LISTAGEM =====\n')
    
    if len(lista) > 0:
        for i in lista:
            for chave, valor in i.items():
                print(chave.upper() + ':', valor)
            print('-----------\n')
    else:
        nome_menu_operacoes = valida_opcao_menu_principal(opcoes_menu_principal)
        print(f'Não há {nome_menu_operacoes} cadastrados.\n')
    
    input('Pressione ENTER para continuar.\n')

# FUNÇÃO ATUALIZAR CADASTRO
def atualizar_cadastro(opcao_menu_principal, codigo, nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    
    for item in lista:
        if item["codigo"] == codigo:
            if opcao_menu_principal == 1 or opcao_menu_principal == 2:
                item["nome"] = input('Informe o novo nome: ')
                item["cpf"] = input('Informe o novo CPF: ')
                salvar_arquivo(lista, nome_arquivo)
                return input('Pressione ENTER para continuar.\n')

            if opcao_menu_principal == 3:
                item["nome"] = int(input('Informe o novo nome da disciplina: '))
                salvar_arquivo(lista, nome_arquivo)
                return input('Pressione ENTER para continuar.\n')

            if opcao_menu_principal == 4:
                item["codigo_turma"] = int(input('Informe o novo codigo da turma: '))
                item["codigo_professor"] = int(input('Informe o novo codigo do professor: '))
                item["codigo_disciplina"] = int(input('Informe o novo codigo da disciplina: '))
                salvar_arquivo(lista, nome_arquivo)
                return input('Pressione ENTER para continuar.\n')

            if opcao_menu_principal == 5:
                item["codigo_turma"] = int(input('Informe o novo codigo da turma: '))
                item["codigo_estudante"] = int(input('Informe o novo codigo do estudante: '))
                return input('Pressione ENTER para continuar.\n')
    
    print('Código não encontrado.')
    input('Pressione ENTER para continuar.\n')
    

# FUNÇÃO EXCLUIR CADASTRO
def excluir_cadastro(opcao, codigo, nome_arquivo):
    item_para_remover = None
    lista = ler_arquivo(nome_arquivo)

    if opcao == 1 or opcao == 2 or opcao == 3:
        for item in lista:
            if item["codigo"] == codigo:
                item_para_remover = item
                break
    elif opcao == 4:
        for item in lista:
            if item["codigo_turma"] == codigo:
                item_para_remover = item
                break
    elif opcao == 5:
        for item in lista:
            if item["codigo_matricula"] == codigo:
                item_para_remover = item
                break


    if item_para_remover is not None:
        lista.remove(item_para_remover)
        salvar_arquivo(lista, nome_arquivo)
    else:
        print("Código não encontrado.")  

# FUNÇÃO ESCREVER/SALVAR ARQUIVO JSON
def salvar_arquivo(lista_qualquer, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista_qualquer, arquivo_aberto, ensure_ascii=False)

# FUNÇÃO LER ARQUIVO JSON
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_qualquer = json.load(arquivo_aberto)
    except:
        return []

    return lista_qualquer

# FUNÇÃO PARA ATUALIZAR ARQUIVO JSON
def atualiza_arquivo(dicionario, nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    lista.append(dicionario)
    salvar_arquivo(lista, nome_arquivo)

# LOOP MENU PRINCIPAL
while True:
    
    opcoes_menu_principal = menu_principal()

    if opcoes_menu_principal == 0:
        print(f'Você escolheu a opção {opcoes_menu_principal}.\n')
        print('***** PROGRAMA ENCERRADO *****\n')
        break
    elif opcoes_menu_principal > 5:
        print('Opção inválida.')
        print('Digite uma opção válida \n')

    nome_menu_operacoes = valida_opcao_menu_principal(opcoes_menu_principal)
    arquivo = f"{nome_menu_operacoes}.json"

    # LOOP MENU OPERACOES
    while True:
        
        opcoes_menu_operacoes = menu_operacoes(nome_menu_operacoes)

        if opcoes_menu_operacoes == 1:
            inclusao_cadastro(opcoes_menu_principal, arquivo)
        
        elif opcoes_menu_operacoes == 2:
            listar_cadastro(opcoes_menu_operacoes, arquivo)

        elif opcoes_menu_operacoes == 3:
            codigo = int(input('Informe o código para editar: '))
            atualizar_cadastro(opcoes_menu_principal, codigo, arquivo)
        
        elif opcoes_menu_operacoes == 4:
            codigo = int(input('Informe o código para remover: '))
            excluir_cadastro(opcoes_menu_principal, codigo, arquivo)

        elif opcoes_menu_operacoes == 9:
            break
        else:
                print('Opção inválida.')
                print('Digite uma opção válida \n')