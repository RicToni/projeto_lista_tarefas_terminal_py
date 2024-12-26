from datetime import datetime, date
import os

os.system('cls')
tarefas = []


def criar_tarefa():
    while True:
        os.system('cls')
        nome = input('Insira o nome da tarefa -> ')
        if not nome.strip():
            os.system('cls')
            print('O nome da tarefa não pode estar vazio!!')
            input('Pressione <ENTER> e tente novamente.')
            continue
        os.system('cls')
        data_str = input('Insira a data da tarefa (DD/MM/AAAA) -> ')
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y').date()
        except ValueError:
            os.system('cls')
            print('Data inválida, insira no formato (DD/MM/AAAA)')
            input('Pressione <ENTER> e tene novamente.')
            continue
        os.system('cls')
        horario_str = input('Insira o horário da tarefa -> ')
        try:
            horario = datetime.strptime(horario_str, '%H:%M').time()
        except ValueError:
            os.system('cls')
            print('Horário inválido, insira no formato HH:MM')
            input('Pressione <ENTER> e tene novamente.')
            continue
        data_hora = datetime.combine(data, horario)
        os.system('cls')
        descr = input('Descreva brevemente a tarefa -> ')
        if not descr.strip():
            os.system('cls')
            print('A descrição da tarefa não pode estar vazia!!')
            input('Pressione <ENTER> e tente novamente.')
            continue
        os.system('cls')
        prior_str = input('Defina a prioridade: [3]ALTA - [2]MEDIA - [1]BAIXA -> ')
        if prior_str not in ('1','2','3'):
            os.system('cls')
            print('Classificação inválida, escolha entre as seguintes opções: [3]ALTA - [2]MEDIA - [1]BAIXA ')
            input('Pressione <ENTER> e tente novamente.')
            continue
        prior = int(prior_str)
        tarefa = dict(nome = nome, data = data_hora, descr = descr, priori = prior)
        tarefas.append(tarefa)
        os.system('cls')
        print(f'Tarefa "{tarefa["nome"]}" criada com sucesso!!')
        input('Pressione <ENTER> pra voltar ao menu eanteriror!!')
        break
 
    
    # nome = dict(nome = nome, data = data, desc = desc, priori = priori)
    # pass

def listar_tarefas():
    os.system('cls')
    index = 1
    for tarefa in tarefas:
        print(f'''
Tarefa {index}:
--------------------------------
Nome: {tarefa["nome"]}
Data/Hora: {tarefa["data"]}
Descrição: {tarefa["descr"]}
Prioridade: {tarefa["priori"]}
''')
        index += 1
    if len(tarefas) == 0:
        print('Você aiinda não adicionou nenhuma tarefa a lista!')
    input('\nPRESSIONE <ENTER> PARA VOLTAR AO MENU ANTERIOR!')

def remover_tarefa():
    os.system('cls')
    listar_tarefas()
    while True:
        try:
            opcao = int(input('Escolha qual tarefa deseja excluir(número da tarefa)? -> '))
            tarefa_excluida = tarefas.pop(opcao - 1)
            os.system('cls')
            print(F'A tarefa {opcao}:{tarefa_excluida["nome"]} foi removida!!')
            break
        except IndexError:
            os.system('cls')
            input('Índice inválido, digite <ENTER> e tente novamente!!!')
        except ValueError:
            os.system('cls')
            input('Entrada inválida! Digite apenas números. pressione <ENTER> e tente novamente!!')  

def exibir_menu():
    os.system('cls')
    print('''
===== GERENCIADOR DE TAREFAS =====
1) - Adicionar tarefa.
2) - Listar tarefas.
3) - Remover tarefa.
4) - Editar tarefa.
5) - Finalizar tarefa .                  
----------------------------------- ''')
    opcao = input('->')
    if opcao not in ('1','2','3','4','5'):
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
        
    elif opcao == '1':
        criar_tarefa()
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        remover_tarefa()
    elif opcao == '4':
        pass